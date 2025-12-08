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

    def fetch_paper_data_stable(self, target_config, identifier, sort_mode):
        """
        极稳健的分页下载：小批量 + 原地重试
        """
        name = target_config["name"]
        strict_names = target_config["strict_names"]
        tag = "最新" if sort_mode == "mostrecent" else "高引"
        
        results = []
        seen_dois = set()  # 本模式内去重
        page = 1
        total_checked = 0  # 统计所有检索的文章总数
        
        base_params = {
            "q": f"a {identifier}", 
            "sort": sort_mode,
            "size": BATCH_SIZE
        }
        
        print(f"\n   [⏳] {name} [{tag}] 开始扫描 (目标 {LIMIT} 篇)...", flush=True)
        
        # 循环直到凑够数量或翻页过多
        while len(results) < LIMIT:
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
                if len(results) >= LIMIT: break
                
                total_checked += 1  # 计数所有检索的文章
                
                metadata = hit.get("metadata", {})
                authors_list = metadata.get("authors", [])
                
                # 1. 过滤大型合作组
                if len(authors_list) > MAX_AUTHORS: 
                    continue
                
                # 2. 严格名字匹配
                if not self.check_exact_match(authors_list, strict_names):
                    continue
                
                # 3. 期刊过滤 (PRD/PRL/Nature/Science)
                d_list = metadata.get("dois", [])
                doi_val = d_list[0].get("value") if d_list else None
                is_allowed_journal = any(journal in doi_val for journal in ALLOWED_JOURNALS) if doi_val else False
                if not is_allowed_journal:
                    continue
                
                # 4. 去重检查（仅本模式内）
                if doi_val in seen_dois:
                    continue
                
                # 5. 提取数据
                if doi_val:
                    author_names = [a.get("full_name", "Unknown") for a in authors_list]
                    authors_str = "; ".join(author_names)
                    
                    results.append({
                        "doi": doi_val,
                        "authors": authors_str
                    })
                    seen_dois.add(doi_val)
                    print(f"      ✓ [{tag}] 第 {total_checked} 篇: {doi_val} (已保存 {len(results)}/{LIMIT})", flush=True)
            
            page += 1
            if page > MAX_PAGES: break # 防止死循环

        print(f"      [⬇️] {name} [{tag}] 完成! 获取 {len(results)} 条", flush=True)
        return sort_mode, results

# ================= ▶️ 辅助函数 =================

def get_processed_teachers(results_file):
    """从 results.txt 中读取已处理的中文姓名列表"""
    processed = set()
    if not os.path.exists(results_file):
        return processed
    
    try:
        with open(results_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 检查是否是等号分隔行
                if line and not line.startswith('=') and not line.startswith('10.'):
                    # 这应该是中文姓名
                    processed.add(line)
    except Exception as e:
        print(f"读取已处理教师列表失败: {e}")
    
    return processed

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
    
    # 1. 读取已处理的教师列表
    processed_teachers = get_processed_teachers(OUTPUT_PATH)
    print(f"📋 已处理教师: {len(processed_teachers)} 人")
    if processed_teachers:
        print(f"   {', '.join(processed_teachers)}\n")
    
    # 2. 从 id.txt 加载 TARGETS
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
    
    # 3. 找到第一个未处理的教师
    target = get_first_unprocessed_target(TARGETS, processed_teachers)
    
    if not target:
        print("\n✅ 所有教师都已处理完成！")
        exit(0)
    
    print(f"\n🎯 本次处理教师: {target.get('cn_name')} ({target.get('name')})\n")
    print("-" * 60)
    
    # 4. 获取该教师的 BAI
    identifier = fetcher.get_bai_from_record_id(target["name"], target["id"])
    if not identifier:
        print(f"❌ 无法获取教师 {target['name']} 的标识符")
        exit(1)
    
    # 5. 并发下载该教师的数据
    print(f"\n⚡ 开始下载与筛选...\n")
    
    final_data = {}
    final_data[target["name"]] = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_map = {}
        f1 = executor.submit(fetcher.fetch_paper_data_stable, target, identifier, "mostrecent")
        future_map[f1] = "mostrecent"
        f2 = executor.submit(fetcher.fetch_paper_data_stable, target, identifier, "mostcited")
        future_map[f2] = "mostcited"
        
        for future in concurrent.futures.as_completed(future_map):
            mode = future_map[future]
            try:
                _, data_list = future.result()
                final_data[target["name"]][mode] = data_list
            except Exception as e:
                print(f"任务异常: {e}")
                final_data[target["name"]][mode] = []

    # 6. 追加写入文件（极简格式：中文名 + 20个DOI）
    print(f"\n{'='*60}")
    print("📝 正在追加写入结果文件...")
    print(f"{'='*60}\n")
    
    try:
        # 使用追加模式
        with open(OUTPUT_PATH, "a", encoding="utf-8") as f:
            name = target["name"]
            cn_name = target.get("cn_name", name)
            
            # 合并最新和高引的所有 DOI
            all_dois = []
            recents = final_data[name].get("mostrecent", [])
            cited = final_data[name].get("mostcited", [])
            
            for item in recents:
                all_dois.append(item['doi'])
            for item in cited:
                all_dois.append(item['doi'])
            
            # 输出：等号 + 中文名 + 等号 + 最多20个DOI
            f.write("=" * 50 + "\n")
            f.write(f"{cn_name}\n")
            f.write("=" * 50 + "\n")
            for doi in all_dois[:20]:  # 只取前20个
                f.write(f"{doi}\n")
            f.write("\n")  # 空行分隔
        
        print(f"✅ 追加完成！")
        print(f"📂 已为 {cn_name} 添加 {min(len(all_dois), 20)} 篇论文")
        print(f"📂 结果文件: {OUTPUT_PATH}")
        
    except Exception as e:
        print(f"❌ 写入失败: {e}")