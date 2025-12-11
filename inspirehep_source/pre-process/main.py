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
FINISHED_TEACHERS_PATH = os.path.join(OUTPUT_DIR, "finished_teachers.txt")

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

    def fetch_paper_data_dual(self, target_config, identifier, sort_mode, 
                              target_limit_restricted=10, existing_dois=None):
        """
        同时收集限制期刊和非限制期刊的论文
        
        返回: (sort_mode, restricted_dois, unrestricted_dois)
        """
        name = target_config["name"]
        strict_names = target_config["strict_names"]
        tag = "最新" if sort_mode == "mostrecent" else "高引"
        
        restricted_results = []  # 限制期刊
        unrestricted_results = []  # 非限制期刊
        seen_dois = set()  # 全局去重
        
        if existing_dois is None:
            existing_dois = set()
        
        page = 1
        total_checked = 0
        
        base_params = {
            "q": f"a {identifier}",
            "sort": sort_mode,
            "size": BATCH_SIZE
        }
        
        print(f"\n   [⏳] {name} [{tag}] 开始扫描 (限制期刊目标 {target_limit_restricted} 篇，同时收集所有非限制期刊，搜索上限 {MAX_PAGES} 页)...", flush=True)
        
        # 循环直到达到搜索上限（不再提前停止）
        while page <= MAX_PAGES:
            params = base_params.copy()
            params["page"] = page
            
            # 原地重试逻辑
            success = False
            for attempt in range(MAX_RETRIES):
                try:
                    res = self.session.get(f"{self.BASE_URL}/literature", params=params, timeout=TIMEOUT)
                    data = res.json()
                    success = True
                    break
                except Exception as e:
                    print(f"      [⚠️] {name} Page {page} 失败 (尝试 {attempt+1}/{MAX_RETRIES}): {e}", flush=True)
                    time.sleep(0.3)
            
            if not success:
                print(f"      [❌] {name} Page {page} 彻底失败，跳过此页", flush=True)
                page += 1
                continue
            
            # 数据处理
            hits = data.get("hits", {}).get("hits", [])
            if not hits:
                print(f"      [ℹ️] {name} Page {page} 无更多数据，搜索完成", flush=True)
                break
            
            for hit in hits:
                total_checked += 1
                
                metadata = hit.get("metadata", {})
                authors_list = metadata.get("authors", [])
                
                # 1. 过滤大型合作组
                if len(authors_list) > MAX_AUTHORS:
                    continue
                
                # 2. 严格名字匹配（确保所有论文都经过严格审查）
                if not self.check_exact_match(authors_list, strict_names):
                    continue
                
                # 3. 提取 DOI
                d_list = metadata.get("dois", [])
                doi_val = d_list[0].get("value") if d_list else None
                
                if not doi_val:
                    continue
                
                # 4. 去重检查（全局去重）
                if doi_val in seen_dois or doi_val in existing_dois:
                    continue
                
                # 5. 判断期刊类型
                is_allowed_journal = any(journal in doi_val for journal in ALLOWED_JOURNALS)
                
                # 6. 添加到对应列表
                author_names = [a.get("full_name", "Unknown") for a in authors_list]
                authors_str = "; ".join(author_names)
                
                result_item = {
                    "doi": doi_val,
                    "authors": authors_str
                }
                
                seen_dois.add(doi_val)
                
                if is_allowed_journal and len(restricted_results) < target_limit_restricted:
                    restricted_results.append(result_item)
                    print(f"      ✓ [{tag}] 限制期刊 第 {total_checked} 篇: {doi_val} (已保存 {len(restricted_results)}/{target_limit_restricted})", flush=True)
                elif not is_allowed_journal:
                    unrestricted_results.append(result_item)
                    print(f"      ✓ [{tag}] 非限制期刊: {doi_val} (已保存 {len(unrestricted_results)})", flush=True)
            
            page += 1
        
        print(f"      [⬇️] {name} [{tag}] 完成! 限制期刊 {len(restricted_results)} 条，非限制期刊 {len(unrestricted_results)} 条", flush=True)
        return sort_mode, restricted_results, unrestricted_results


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
    
    # 5. 第一阶段：获取最新和高引（各限制期刊10篇 + 所有非限制期刊）
    print(f"\n⚡ 第一阶段：获取限制期刊和非限制期刊论文...\n")
    
    final_data = {}
    final_data[target["name"]] = {}
    name = target["name"]
    cn_name = target.get("cn_name", name)
    
    # 并发获取 mostrecent 和 mostcited，同时收集限制和非限制期刊
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_map = {}
        f1 = executor.submit(
            fetcher.fetch_paper_data_dual,
            target, identifier, "mostrecent",
            target_limit_restricted=10,
            existing_dois=None
        )
        future_map[f1] = "mostrecent"
        
        f2 = executor.submit(
            fetcher.fetch_paper_data_dual,
            target, identifier, "mostcited",
            target_limit_restricted=10,
            existing_dois=None
        )
        future_map[f2] = "mostcited"
        
        for future in concurrent.futures.as_completed(future_map):
            mode = future_map[future]
            try:
                _, restricted_list, unrestricted_list = future.result()
                final_data[name][mode] = {
                    "restricted": restricted_list,
                    "unrestricted": unrestricted_list
                }
            except Exception as e:
                print(f"任务异常: {e}")
                final_data[name][mode] = {
                    "restricted": [],
                    "unrestricted": []
                }
    
    # 6. 合并并去重限制期刊 DOI
    restricted_dois = []
    restricted_dois_unique = []
    restricted_seen = set()
    
    unrestricted_dois = []  # 收集所有非限制期刊 DOI
    unrestricted_seen = set()
    
    # 处理 mostrecent 的限制期刊
    recents = final_data[name].get("mostrecent", {})
    for item in recents.get("restricted", []):
        doi = item['doi']
        restricted_dois.append(doi)
        if doi not in restricted_seen:
            restricted_dois_unique.append(doi)
            restricted_seen.add(doi)
    
    # 处理 mostcited 的限制期刊
    cited = final_data[name].get("mostcited", {})
    for item in cited.get("restricted", []):
        doi = item['doi']
        restricted_dois.append(doi)
        if doi not in restricted_seen:
            restricted_dois_unique.append(doi)
            restricted_seen.add(doi)
    
    # 收集所有非限制期刊 DOI（从 mostrecent 和 mostcited）
    for item in recents.get("unrestricted", []):
        doi = item['doi']
        if doi not in unrestricted_seen:
            unrestricted_dois.append(doi)
            unrestricted_seen.add(doi)
    
    for item in cited.get("unrestricted", []):
        doi = item['doi']
        if doi not in unrestricted_seen:
            unrestricted_dois.append(doi)
            unrestricted_seen.add(doi)
    
    # 检查限制期刊是否有重复
    if len(restricted_dois_unique) < len(restricted_dois):
        print(f"\n⚠️ 限制期刊发现重复 DOI：收集 {len(restricted_dois)} 篇，去重后 {len(restricted_dois_unique)} 篇")
    
    supplement_mode = False
    cited_supplement = []  # 初始化补充数据
    
    # 如果限制期刊不足 20 篇，启动补充模式（仅在高引限制期刊中补充）
    if len(restricted_dois_unique) < 20:
        supplement_mode = True
        existing_restricted_dois = set(restricted_dois_unique)
        needed = 20 - len(restricted_dois_unique)
        
        print(f"\n⚠️ 限制期刊仅获取 {len(restricted_dois_unique)} 篇，不足 20 篇")
        print(f"🔄 启动补充模式：从高引限制期刊补充 {needed} 篇...\n")
        
        # 第二阶段：仅从 mostcited 的限制期刊补充
        _, cited_restricted, _ = fetcher.fetch_paper_data_dual(
            target, identifier, "mostcited",
            target_limit_restricted=needed,
            existing_dois=existing_restricted_dois
        )
        cited_supplement = cited_restricted
        
        # 追加到限制期刊数据
        restricted_dois_unique.extend([item['doi'] for item in cited_supplement])
    
    # 7. 写入文件
    print(f"\n{'='*60}")
    print("📝 正在写入结果文件...")
    print(f"{'='*60}\n")
    
    try:
        with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
            # 第一条目：限制期刊 DOI（不带加号）
            f.write("=" * 50 + "\n")
            f.write(f"{cn_name}\n")
            f.write("=" * 50 + "\n")
            
            # 输出限制期刊的 DOI，最多 20 篇
            output_restricted = restricted_dois_unique[:20]
            for doi in output_restricted:
                f.write(f"{doi}\n")
            f.write("\n")
            
            print(f"✅ 第一条目完成！")
            print(f"📂 限制期刊：{cn_name} 添加 {len(output_restricted)} 篇论文")
            
            if supplement_mode:
                print(f"📂 补充模式已使用：从高引限制期刊补充 {len(cited_supplement)} 篇")
            
            # 第二条目：非限制期刊 DOI（名字后加+）
            if unrestricted_dois:
                f.write("=" * 50 + "\n")
                f.write(f"{cn_name}+\n")
                f.write("=" * 50 + "\n")
                
                for doi in unrestricted_dois:
                    f.write(f"{doi}\n")
                f.write("\n")
                
                print(f"📂 第二条目完成！")
                print(f"📂 非限制期刊：{cn_name}+ 添加 {len(unrestricted_dois)} 篇论文")
        
        print(f"📂 结果文件: {OUTPUT_PATH}")
        
        # 追加教师名到 finished_teachers.txt
        try:
            with open(FINISHED_TEACHERS_PATH, "a", encoding="utf-8") as f:
                f.write(f"{cn_name}\n")
            print(f"✅ 已将 {cn_name} 追加到 finished_teachers.txt")
        except Exception as e:
            print(f"⚠️ 写入 finished_teachers.txt 失败: {e}")
        
    except Exception as e:
        print(f"❌ 写入失败: {e}")
        import traceback
        traceback.print_exc()
