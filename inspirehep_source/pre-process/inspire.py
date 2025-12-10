import os
import requests
import concurrent.futures
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ================= ⚙️ 配置区域 =================

# 1. 目标作者配置
TARGETS = [
    {
        "name": "Feng, Xu",
        "id": "1040303",
        "cn_name": "冯旭",
        "strict_names": ["Xu, Feng"]
    },
]

# 2. 数量限制
LIMIT = 10       
MAX_AUTHORS = 10 # 过滤掉作者数超过 10 人的文章

# 2.5 期刊限制
ALLOWED_JOURNALS = ["PhysRevD", "PhysRevLett", "Nature", "Science"]  # 只收集 PRD/PRL/Nature/Science 的论文

# 3. 网络请求配置 (优化版)
BATCH_SIZE = 50  # 每次抓 50 篇，大幅提高下载速度
MAX_RETRIES = 2  # 单页失败重试次数
MAX_PAGES = 30   # 最多翻 30 页
TIMEOUT = 8      # 降低超时时间到 8 秒

# 4. 输出路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = CURRENT_DIR
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "results.txt")

# ================= 🛠️ 核心代码 =================

class StableFetcher:
    BASE_URL = "https://inspirehep.net/api"
    
    def __init__(self):
        self.session = requests.Session()
        # 底层 TCP 重试策略
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json"
        })

    def get_bai_from_record_id(self, name, record_id):
        """获取 BAI"""
        print(f"   [🔍] 访问档案 ID: {record_id} ({name})...")
        try:
            res = self.session.get(f"{self.BASE_URL}/authors/{record_id}", timeout=20)
            if res.status_code == 404: return None
            data = res.json()
            ids = data.get("metadata", {}).get("ids", [])
            bai = next((item.get("value") for item in ids if item.get("schema") == "INSPIRE BAI"), None)
            return bai if bai else f"recid:{record_id}"
        except Exception: return None

    def check_exact_match(self, paper_authors, strict_names):
        """灵活的名字匹配：支持不同的名字顺序、空格变体等"""
        for author in paper_authors:
            full_name = author.get("full_name", "").strip()
            full_name_lower = full_name.lower()
            
            for strict_name in strict_names:
                strict_name_lower = strict_name.lower()
                
                # 1. 直接完全匹配
                if full_name_lower == strict_name_lower:
                    return True
                
                # 2. 处理空格变体：移除所有空格后比较
                # 例如 "HuaXing, Zhu" 应该匹配 "Hua Xing, Zhu"
                strict_no_space = strict_name_lower.replace(" ", "")
                full_no_space = full_name_lower.replace(" ", "")
                
                if strict_no_space == full_no_space:
                    return True
                
                # 3. 处理名字顺序变体（都含有逗号）
                if ',' in strict_name_lower and ',' in full_name_lower:
                    strict_parts = [p.strip() for p in strict_name_lower.split(',')]
                    full_parts = [p.strip() for p in full_name_lower.split(',')]
                    
                    if len(strict_parts) == 2 and len(full_parts) == 2:
                        # 检查是否是反向顺序
                        if strict_parts[0] == full_parts[1] and strict_parts[1] == full_parts[0]:
                            return True
                        
                        # 处理顺序反转时的空格变体
                        strict_parts_no_space = [p.replace(" ", "") for p in strict_parts]
                        full_parts_no_space = [p.replace(" ", "") for p in full_parts]
                        if (strict_parts_no_space[0] == full_parts_no_space[1] and 
                            strict_parts_no_space[1] == full_parts_no_space[0]):
                            return True
                
                # 4. 如果 strict_name 中没有逗号，尝试从 full_name 中提取匹配
                if ',' not in strict_name_lower and ',' in full_name_lower:
                    # 例如 strict_name="Xu Feng"，full_name="Feng, Xu"
                    parts = strict_name_lower.split()
                    # 检查 strict_name 的各部分是否都在 full_name 中
                    if all(part in full_name_lower for part in parts):
                        return True
                    
                    # 也处理空格移除后的匹配
                    parts_no_space = [p.replace(" ", "") for p in parts]
                    for part_no_space in parts_no_space:
                        if part_no_space and part_no_space not in full_no_space:
                            break
                    else:
                        # 所有部分都匹配
                        if all(p.replace(" ", "") in full_no_space for p in parts):
                            return True
        
        return False

    def fetch_paper_data_stable(self, target_config, identifier, sort_mode, 
                                 allow_all_journals=False, existing_dois=None, target_limit=None):
        """
        极稳健的分页下载：小批量 + 原地重试
        
        参数:
            target_config: 目标配置字典
            identifier: 作者标识符
            sort_mode: 排序模式 (mostrecent/mostcited)
            allow_all_journals: 是否允许所有期刊（补充模式用，默认 False）
            existing_dois: 已有 DOI 集合，用于去重（默认 None）
            target_limit: 目标数量（默认使用LIMIT）
        """
        name = target_config["name"]
        strict_names = target_config["strict_names"]
        tag = "最新" if sort_mode == "mostrecent" else "高引"
        
        results = []
        seen_dois = set()  # 本模式内去重
        if existing_dois is None:
            existing_dois = set()  # 防止 None
        
        if target_limit is None:
            target_limit = LIMIT
        
        page = 1
        total_checked = 0  # 统计所有检索的文章总数
        
        base_params = {
            "q": f"a {identifier}", 
            "sort": sort_mode,
            "size": BATCH_SIZE
        }
        
        mode_tag = "[补充]" if allow_all_journals else ""
        print(f"\n   [⏳] {name} [{tag}]{mode_tag} 开始扫描 (目标 {target_limit} 篇)...", flush=True)
        
        # 循环直到凑够数量或翻页过多
        while len(results) < target_limit:
            params = base_params.copy()
            params["page"] = page
            
            # --- 原地重试逻辑 ---
            success = False
            for attempt in range(MAX_RETRIES):
                try:
                    res = self.session.get(f"{self.BASE_URL}/literature", params=params, timeout=TIMEOUT)
                    data = res.json()
                    success = True
                    break # 成功则跳出重试循环
                except Exception as e:
                    print(f"      [⚠️] {name} Page {page} 失败 (尝试 {attempt+1}/{MAX_RETRIES}): {e}", flush=True)
                    time.sleep(0.3) # 缩短等待时间
            
            if not success:
                print(f"      [❌] {name} Page {page} 彻底失败，跳过此页", flush=True)
                page += 1
                continue # 放弃这一页，尝试下一页
            
            # --- 数据处理 ---
            hits = data.get("hits", {}).get("hits", [])
            if not hits: 
                break # 没有更多数据了
            
            for hit in hits:
                if len(results) >= target_limit: break
                
                total_checked += 1  # 计数所有检索的文章
                
                metadata = hit.get("metadata", {})
                authors_list = metadata.get("authors", [])
                
                # 1. 过滤大型合作组
                if len(authors_list) > MAX_AUTHORS: 
                    continue
                
                # 2. 严格名字匹配
                if not self.check_exact_match(authors_list, strict_names):
                    continue
                
                # 3. 提取 DOI
                d_list = metadata.get("dois", [])
                doi_val = d_list[0].get("value") if d_list else None
                
                if not doi_val:
                    continue
                
                # 4. 期刊过滤 (仅在非补充模式下)
                if not allow_all_journals:
                    is_allowed_journal = any(journal in doi_val for journal in ALLOWED_JOURNALS)
                    if not is_allowed_journal:
                        continue
                
                # 5. 去重检查（本模式内 + 已有 DOI）
                if doi_val in seen_dois or doi_val in existing_dois:
                    continue
                
                # 6. 添加结果
                author_names = [a.get("full_name", "Unknown") for a in authors_list]
                authors_str = "; ".join(author_names)
                
                results.append({
                    "doi": doi_val,
                    "authors": authors_str
                })
                seen_dois.add(doi_val)
                print(f"      ✓ [{tag}]{mode_tag} 第 {total_checked} 篇: {doi_val} (已保存 {len(results)}/{target_limit})", flush=True)
            
            page += 1
            if page > MAX_PAGES: break # 防止死循环

        print(f"      [⬇️] {name} [{tag}]{mode_tag} 完成! 获取 {len(results)} 条", flush=True)
        return sort_mode, results

# ================= ▶️ 辅助函数 =================

def parse_results_file(results_file):
    """
    解析 results.txt，返回教师信息字典
    返回格式: {
        "cn_name": {
            "completed": True/False,  # 是否有星号
            "dois": ["doi1", "doi2", ...],
            "line_start": 行号  # 名字所在行号
        }
    }
    """
    teachers_info = {}
    
    if not os.path.exists(results_file):
        return teachers_info
    
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        current_teacher = None
        line_num = 0
        
        for idx, line in enumerate(lines):
            line_stripped = line.strip()
            
            # 跳过空行和等号行
            if not line_stripped or line_stripped.startswith('='):
                continue
            
            # 检查是否是 DOI
            if line_stripped.startswith('10.'):
                if current_teacher:
                    teachers_info[current_teacher]["dois"].append(line_stripped)
            else:
                # 这是教师名字
                completed = line_stripped.endswith('+')
                cn_name = line_stripped.rstrip('+').strip()
                
                current_teacher = cn_name
                teachers_info[cn_name] = {
                    "completed": completed,
                    "dois": [],
                    "line_number": idx
                }
    
    except Exception as e:
        print(f"解析 results.txt 失败: {e}")
    
    return teachers_info

def get_processed_teachers(results_file):
    """从 results.txt 中读取已处理的中文姓名列表（不含星号的原始名字）"""
    processed = set()
    if not os.path.exists(results_file):
        return processed
    
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 检查是否是等号分隔行或 DOI
                if line and not line.startswith('=') and not line.startswith('10.'):
                    # 移除可能的星号，这是中文姓名
                    cn_name = line.rstrip('+').strip()
                    processed.add(cn_name)
    except Exception as e:
        print(f"读取已处理教师列表失败: {e}")
    
    return processed

def find_teacher_needing_supplement(results_file):
    """
    找到第一个需要补充论文的教师（没有星号的教师）
    返回: (cn_name, existing_dois) 或 (None, None)
    """
    teachers_info = parse_results_file(results_file)
    
    for cn_name, info in teachers_info.items():
        if not info["completed"]:
            return cn_name, set(info["dois"])
    
    return None, None

def update_teacher_status_in_file(results_file, cn_name, mark_completed=True):
    """
    在 results.txt 中给教师名字添加或移除补充标记（尾部+）
    mark_completed=True: 添加+
    mark_completed=False: 移除+
    """
    if not os.path.exists(results_file):
        return
    
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        for idx, line in enumerate(lines):
            line_stripped = line.strip()
            # 跳过空行和等号
            if not line_stripped or line_stripped.startswith('=') or line_stripped.startswith('10.'):
                continue
            
            # 获取不含补充标记的名字
            current_name = line_stripped.rstrip('+').strip()
            
            if current_name == cn_name:
                if mark_completed and not line_stripped.endswith('+'):
                    # 添加补充标记（放在名字后）
                    lines[idx] = current_name + '+\n'
                    modified = True
                elif not mark_completed and line_stripped.endswith('+'):
                    # 移除补充标记
                    lines[idx] = current_name + '\n'
                    modified = True
                break
        
        if modified:
            with open(results_file, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            status = "已完成" if mark_completed else "未完成"
            print(f"   ✓ 已标记 {cn_name} 为 {status}")
    
    except Exception as e:
        print(f"更新教师状态失败: {e}")

def get_first_unprocessed_target(targets, processed_names):
    """从 TARGETS 中获取第一个未处理的教师"""
    for target in targets:
        cn_name = target.get('cn_name', '')
        if cn_name and cn_name not in processed_names:
            return target
    return None

# ================= ▶️ 主程序 =================

if __name__ == "__main__":
    # 自动创建目录
    if not os.path.exists(OUTPUT_DIR):
        try:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            print(f"📂 已创建目录: {OUTPUT_DIR}")
        except OSError as e:
            print(f"❌ 创建目录失败: {e}")
            exit(1)

    fetcher = StableFetcher()
    
    print(f"🚀 启动增量模式 (Batch={BATCH_SIZE}, Limit={LIMIT})...")
    print(f"📄 输出文件: {OUTPUT_PATH}\n")
    
    # 1. 从 id.txt 加载 TARGETS
    id_file_path = os.path.join(CURRENT_DIR, "id.txt")
    if os.path.exists(id_file_path):
        try:
            with open(id_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 执行 id.txt 获取 TARGETS
                local_vars = {}
                exec(content, {}, local_vars)
                if 'TARGETS' in local_vars:
                    TARGETS = local_vars['TARGETS']
                    print(f"✓ 从 id.txt 加载了 {len(TARGETS)} 个目标教师")
        except Exception as e:
            print(f"⚠️ 无法加载 id.txt，使用默认 TARGETS: {e}")
    
    # 2. 读取已处理的教师列表
    processed_teachers = get_processed_teachers(OUTPUT_PATH)
    print(f"📋 已处理教师: {len(processed_teachers)} 人")
    if processed_teachers:
        print(f"   {', '.join(processed_teachers)}\n")
    
    # 3. 找第一个未处理的新教师
    target = get_first_unprocessed_target(TARGETS, processed_teachers)
    
    if not target:
        print("\n✅ 所有教师都已处理完成！")
        exit(0)
    
    print(f"\n🎯 新教师: {target.get('cn_name')} ({target.get('name')})\n")
    print("-" * 60)
    
    # 4. 获取该教师的 BAI
    identifier = fetcher.get_bai_from_record_id(target["name"], target["id"])
    if not identifier:
        print(f"❌ 无法获取教师 {target['name']} 的标识符")
        exit(1)
    
    # 5. 第一阶段：使用期刊限制下载（最新和高引各10篇）
    print(f"\n⚡ 第一阶段：限制期刊下载（最新10篇 + 高引10篇）...\n")
    
    final_data = {}
    final_data[target["name"]] = {}
    name = target["name"]
    cn_name = target.get("cn_name", name)
    
    # 并发获取 mostrecent 和 mostcited，各10篇
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_map = {}
        f1 = executor.submit(
            fetcher.fetch_paper_data_stable,
            target, identifier, "mostrecent",
            allow_all_journals=False,
            existing_dois=None,
            target_limit=10  # 最新10篇
        )
        future_map[f1] = "mostrecent"
        
        f2 = executor.submit(
            fetcher.fetch_paper_data_stable,
            target, identifier, "mostcited",
            allow_all_journals=False,
            existing_dois=None,
            target_limit=10  # 高引10篇
        )
        future_map[f2] = "mostcited"
        
        for future in concurrent.futures.as_completed(future_map):
            mode = future_map[future]
            try:
                _, data_list = future.result()
                final_data[name][mode] = data_list
            except Exception as e:
                print(f"任务异常: {e}")
                final_data[name][mode] = []
    
    # 6. 合并第一阶段的 DOI 并进行去重
    all_dois = []
    all_dois_unique = []  # 去重后的 DOI
    seen_dois_set = set()
    
    recents = final_data[name].get("mostrecent", [])
    cited = final_data[name].get("mostcited", [])
    
    for item in recents:
        doi = item['doi']
        all_dois.append(doi)
        if doi not in seen_dois_set:
            all_dois_unique.append(doi)
            seen_dois_set.add(doi)
    
    for item in cited:
        doi = item['doi']
        all_dois.append(doi)
        if doi not in seen_dois_set:
            all_dois_unique.append(doi)
            seen_dois_set.add(doi)
    
    # 检查是否有重复
    if len(all_dois_unique) < len(all_dois):
        print(f"\n⚠️ 第一阶段发现重复 DOI：收集 {len(all_dois)} 篇，去重后 {len(all_dois_unique)} 篇")
    
    supplement_mode = False
    cited_supplement = []  # 初始化补充数据
    
    # 如果去重后不足 20 篇，启动补充模式
    if len(all_dois_unique) < 20:
        supplement_mode = True
        existing_dois = set(all_dois_unique)
        needed = 20 - len(all_dois_unique)
        
        print(f"\n⚠️ 去重后仅获取 {len(all_dois_unique)} 篇，不足 20 篇")
        print(f"🔄 启动补充模式：无期刊限制，仅从高引补充 {needed} 篇...\n")
        
        # 第二阶段：无期刊限制，仅从 mostcited 补充
        _, cited_supplement = fetcher.fetch_paper_data_stable(
            target, identifier, "mostcited",
            allow_all_journals=True,
            existing_dois=existing_dois,
            target_limit=needed
        )
        
        # 追加到 mostcited 数据
        final_data[name]["mostcited"].extend(cited_supplement)
        
        # 重新合并所有 DOI
        all_dois = []
        recents = final_data[name].get("mostrecent", [])
        cited = final_data[name].get("mostcited", [])
        
        for item in recents:
            all_dois.append(item['doi'])
        for item in cited:
            all_dois.append(item['doi'])
    
    # 7. 写入文件
    print(f"\n{'='*60}")
    print("📝 正在写入结果文件...")
    print(f"{'='*60}\n")
    
    try:
        with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
            if supplement_mode:
                # 补充模式：分两个条目写入
                
                # 第一条目：第一阶段的结果（不带星号，去重后）
                phase1_dois_unique = []
                phase1_seen = set()
                
                recents = final_data[name].get("mostrecent", [])
                cited_phase1 = final_data[name].get("mostcited", [])
                
                # 只取第一阶段的数据（需要区分第一阶段和补充阶段）
                # 通过长度判断：mostrecent 都是第一阶段，mostcited 可能混合
                for item in recents:
                    doi = item['doi']
                    if doi not in phase1_seen:
                        phase1_dois_unique.append(doi)
                        phase1_seen.add(doi)
                
                # mostcited 中，前 len(all_dois_before_supplement) 是第一阶段
                all_dois_before_supplement_count = len(all_dois_unique)
                recents_count = len(recents)
                cited_phase1_count = all_dois_before_supplement_count - recents_count
                
                for i, item in enumerate(cited_phase1[:cited_phase1_count]):
                    doi = item['doi']
                    if doi not in phase1_seen:
                        phase1_dois_unique.append(doi)
                        phase1_seen.add(doi)
                
                # 写入第一阶段（不带标记，去重后）
                f.write("=" * 50 + "\n")
                f.write(f"{cn_name}\n")
                f.write("=" * 50 + "\n")
                for doi in phase1_dois_unique:
                    f.write(f"{doi}\n")
                f.write("\n")
                
                # 第二条目：补充阶段的结果（名字后加+）
                supplement_dois = [item['doi'] for item in cited_supplement]
                
                f.write("=" * 50 + "\n")
                f.write(f"{cn_name}+\n")
                f.write("=" * 50 + "\n")
                for doi in supplement_dois:
                    f.write(f"{doi}\n")
                f.write("\n")
                
                print(f"✅ 添加完成！")
                print(f"📂 第一阶段：{cn_name} 添加 {len(phase1_dois_unique)} 篇（期刊限制，已去重）")
                print(f"📂 第二阶段：{cn_name}+ 添加 {len(supplement_dois)} 篇（补充模式）")
                
            else:
                # 无补充模式：只写一个条目（不带星号，去重后）
                f.write("=" * 50 + "\n")
                f.write(f"{cn_name}\n")
                f.write("=" * 50 + "\n")
                
                # 输出去重后的 DOI
                for doi in all_dois_unique[:20]:  # 只取前20个
                    f.write(f"{doi}\n")
                f.write("\n")
                
                print(f"✅ 添加完成！")
                print(f"📂 已为 {cn_name} 添加 {len(all_dois_unique)} 篇论文（期刊限制，已去重）")
        
        print(f"📂 结果文件: {OUTPUT_PATH}")
        
    except Exception as e:
        print(f"❌ 写入失败: {e}")
        import traceback
        traceback.print_exc()
