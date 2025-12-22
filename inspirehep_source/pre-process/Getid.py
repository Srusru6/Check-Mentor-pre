import os
import requests
import json
import time
import re
import configparser
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from pathlib import Path

# 尝试导入 pypinyin，如果没有则提示安装
try:
    from pypinyin import pinyin, Style
except ImportError:
    print("❌ 需要安装 pypinyin 库")
    print("运行: pip install pypinyin")
    exit(1)

# ================= ⚙️ 配置区域 =================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.abspath(os.path.join(CURRENT_DIR, "..", "..", "config.ini"))
TEACHERS_PATH = os.path.join(CURRENT_DIR, "theory_teachers.txt")
FINISHED_PATH = os.path.join(CURRENT_DIR, "finished_teachers.txt")
OUTPUT_PATH = os.path.join(CURRENT_DIR, "id.txt")

# InspireHEP API 配置
BASE_URL = "https://inspirehep.net/api"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 20
SEARCH_SIZE = 100  # 搜索前 100 条结果


def load_preprocess_config():
    """从 config.ini 读取预处理参数，缺失时使用默认值。"""
    parser = configparser.ConfigParser()
    if os.path.exists(CONFIG_PATH):
        try:
            parser.read(CONFIG_PATH, encoding="utf-8")
        except Exception:
            pass
    if not parser.has_section("preprocess"):
        return {}
    section = parser["preprocess"]

    def _get_int(key, default):
        try:
            return int(section.get(key, fallback=default))
        except Exception:
            return default

    return {
        "author_search_size": _get_int("author_search_size", SEARCH_SIZE),
        "author_search_timeout": _get_int("author_search_timeout", REQUEST_TIMEOUT),
        "author_search_retries": _get_int("author_search_retries", MAX_RETRIES),
    }


_cfg = load_preprocess_config()
SEARCH_SIZE = _cfg.get("author_search_size", SEARCH_SIZE)
REQUEST_TIMEOUT = _cfg.get("author_search_timeout", REQUEST_TIMEOUT)
MAX_RETRIES = _cfg.get("author_search_retries", MAX_RETRIES)

# ================= 🛠️ 核心代码 =================

class TargetSearcher:
    def __init__(self):
        self.session = requests.Session()
        # 底层 TCP 重试策略
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json"
        })
    
    def read_teachers(self, file_path):
        """读取老师名单"""
        teachers = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    name = line.strip()
                    if name and not name.startswith('#'):
                        teachers.append(name)
        except FileNotFoundError:
            print(f"❌ 找不到文件: {file_path}")
            return []
        
        return teachers
    
    def search_author(self, cn_name):
        """
        搜索老师，返回前 100 条结果
        """
        print(f"[🔍] 搜索: {cn_name}...", end=" ")
        
        for attempt in range(MAX_RETRIES):
            try:
                # 搜索
                params = {
                    "q": cn_name,
                    "sort": "bestmatch",
                    "size": SEARCH_SIZE,
                    "page": 1
                }
                res = self.session.get(f"{BASE_URL}/authors", params=params, timeout=REQUEST_TIMEOUT)
                
                if res.status_code != 200:
                    print(f"[⚠️] HTTP {res.status_code}，重试...")
                    time.sleep(1)
                    continue
                
                data = res.json()
                hits = data.get("hits", {}).get("hits", [])
                
                print(f"[✓] 找到 {len(hits)} 条结果")
                return {
                    "cn_name": cn_name,
                    "results": hits,
                    "success": True
                }
            
            except Exception as e:
                print(f"[⚠️] 错误: {e}，重试...", end=" ")
                time.sleep(2)
        
        print(f"[❌] 失败")
        return {
            "cn_name": cn_name,
            "results": [],
            "success": False
        }
    
    def get_pinyin_list(self, cn_name):
        """
        获取中文名字的拼音列表
        例如: "曹庆宏" -> ["cao", "qing", "hong"]
        """
        try:
            # 获取每个字的拼音，使用 NORMAL 模式（不带声调）
            pinyin_list = pinyin(cn_name, style=Style.NORMAL)
            # 拼平：[[p1], [p2], ...] -> [p1, p2, ...]
            result = [p[0].lower() for p in pinyin_list if p]
            return result
        except Exception as e:
            print(f"      [⚠️] 获取拼音失败: {e}")
            return []
    
    def check_name_contains_pinyin(self, name, pinyin_list):
        """
        检验 name 是否包含老师名字每个字的拼音
        拼音必须作为连续字符串被检索到，不区分大小写
        """
        if not name or not pinyin_list:
            return False
        
        # 将 name 转换为小写进行匹配
        name_lower = name.lower()
        
        # 检查每个拼音是否作为连续字符串存在于 name 中
        for py in pinyin_list:
            if py not in name_lower:
                return False
        
        return True
    
    def filter_and_verify(self, all_results):
        """
        对搜索结果进行过滤和验证：
        1. 机构过滤：只保留包含 "Peking" 的机构
        2. 拼音检验：检查 name 是否包含老师名字每个字的拼音
        """
        filtered_results = {}
        
        for result in all_results:
            cn_name = result["cn_name"]
            if not result["success"]:
                filtered_results[cn_name] = []
                continue
            
            # 获取拼音列表
            pinyin_list = self.get_pinyin_list(cn_name)
            
            if not pinyin_list:
                print(f"   [⚠️] 跳过拼音检验（无法获取拼音）")
                filtered_results[cn_name] = []
                continue
            
            results_list = []
            
            for idx, hit in enumerate(result["results"], 1):
                record = hit.get("metadata", {})
                
                # 获取名字
                name = record.get("name", {}).get("value")
                
                # 获取 ID
                author_id = hit.get("id")
                
                # 获取机构信息
                positions = record.get("positions", [])
                institution = None
                if positions and len(positions) > 0:
                    pos = positions[0]
                    # 处理 positions[0] 可能是字符串或字典的情况
                    if isinstance(pos, dict):
                        institution = pos.get("institution", {})
                        if isinstance(institution, dict):
                            institution = institution.get("name")
                    elif isinstance(pos, str):
                        institution = pos
                
                # 第一步：机构过滤 - 只保留包含 "Peking" 的
                if not institution or "Peking" not in institution:
                    continue
                
                # 第二步：拼音检验 - 检查 name 是否包含所有拼音
                if not self.check_name_contains_pinyin(name, pinyin_list):
                    continue
                
                # 构建结果信息
                result_info = {
                    "name": name,
                    "id": author_id,
                    "strict_names": self._generate_strict_names(name)
                }
                results_list.append(result_info)
            
            filtered_results[cn_name] = results_list
        
        return filtered_results
    
    def _clean_english_name(self, name_str):
        """
        从名字字符串中去除所有括号和汉字，只保留英文部分
        """
        # 去除括号及其内容
        cleaned = re.sub(r'[（(][^）)]*[）)]', '', name_str)
        # 去除任何剩余的汉字
        cleaned = re.sub(r'[\u4e00-\u9fff]', '', cleaned)
        # 去除多余的空格和逗号
        cleaned = re.sub(r'[\s,]+', ' ', cleaned).strip()
        return cleaned
    
    def _generate_strict_names(self, en_name):
        """
        从英文名生成严格匹配的名字变体
        例如: "Qing-Hong Cao" -> ["Cao, Qing Hong", "Cao, Qing-Hong"]
        """
        # 清理名字，去除括号和汉字
        en_name = self._clean_english_name(en_name)
        
        if not en_name:
            return []
        
        names_set = set()
        
        # 分割名字
        parts = en_name.strip().split()
        
        if len(parts) >= 2:
            # 假设最后一个单词是姓氏
            last_name = parts[-1]
            first_names = " ".join(parts[:-1])
            
            # 格式 1: "LastName, FirstName"（保留连字符）
            names_set.add(f"{last_name}, {first_names}")
            
            # 格式 2: 处理连字符变体
            if "-" in first_names:
                variant_first = first_names.replace("-", " ")
                names_set.add(f"{last_name}, {variant_first}")
        
        # 如果只有一个词，直接返回
        if len(parts) == 1:
            names_set.add(en_name)
        
        return sorted(list(names_set))
    
    def save_targets(self, filtered_results, output_path):
        """
        追加保存最终的 TARGETS 到 id.txt，包含中文名
        """
        # 读取已有的 TARGETS
        existing_targets = []
        if os.path.exists(output_path):
            try:
                with open(output_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                local_vars = {}
                exec(content, {}, local_vars)
                if 'TARGETS' in local_vars:
                    existing_targets = local_vars['TARGETS']
            except Exception as e:
                print(f"[⚠️] 读取现有 TARGETS 失败: {e}")
        
        # 构建新的 targets
        new_targets = []
        for cn_name in sorted(filtered_results.keys()):
            items = filtered_results[cn_name]
            for item in items:
                target = {
                    "name": item["name"],
                    "id": item["id"],
                    "cn_name": cn_name,
                    "strict_names": item["strict_names"]
                }
                new_targets.append(target)
        
        # 合并 existing 和 new
        all_targets = existing_targets + new_targets
        
        # 生成 Python 代码格式的 TARGETS
        targets_code = "TARGETS = [\n"
        for target in all_targets:
            targets_code += "    {\n"
            targets_code += f'        "name": "{target["name"]}",\n'
            targets_code += f'        "id": "{target["id"]}",\n'
            targets_code += f'        "cn_name": "{target["cn_name"]}",\n'
            targets_code += f'        "strict_names": {json.dumps(target["strict_names"], ensure_ascii=False)}\n'
            targets_code += "    },\n"
        targets_code += "]\n"
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(targets_code)
            print(f"\n✅ 已追加保存 TARGETS 到: {output_path}")
            print(f"   原有 {len(existing_targets)} 条，新增 {len(new_targets)} 条，共 {len(all_targets)} 条")
            return len(new_targets)
        except Exception as e:
            print(f"❌ 保存失败: {e}")
            return 0

# 读取已有 id.txt 中的中文名，用于跳过已处理的老师
def read_existing_cn_from_id(id_file):
    existing = set()
    if not os.path.exists(id_file):
        return existing
    try:
        with open(id_file, 'r', encoding='utf-8') as f:
            content = f.read()
        local_vars = {}
        exec(content, {}, local_vars)
        if 'TARGETS' in local_vars:
            for item in local_vars['TARGETS']:
                cn = item.get("cn_name")
                if cn:
                    existing.add(cn)
    except Exception as e:
        print(f"[⚠️] 读取 id.txt 失败，忽略已处理跳过: {e}")
    return existing

# ================= ▶️ 主程序 =================

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 InspireHEP 老师信息搜索与提取")
    print("=" * 60)
    print(f"📄 输入文件: {TEACHERS_PATH}")
    print(f"📄 输出文件: {OUTPUT_PATH}\n")
    
    searcher = TargetSearcher()
    
    # 1. 读取老师列表
    teachers = searcher.read_teachers(TEACHERS_PATH)
    if not teachers:
        print("❌ 无法读取老师列表，程序退出")
        exit(1)

    # 1.1 读取已有 id.txt，跳过已处理老师
    existing_cn = read_existing_cn_from_id(OUTPUT_PATH)
    if existing_cn:
        teachers = [t for t in teachers if t not in existing_cn]
        print(f"[ℹ️] 已跳过 id.txt 中的老师 {len(existing_cn)} 位")

    if not teachers:
        print("✅ 所有老师均已存在 id.txt 中，程序退出")
        exit(0)
    
    print(f"[ℹ️] 本次待处理 {len(teachers)} 位老师\n")
    print("-" * 60)
    
    # 2. 逐个搜索老师
    all_results = []
    
    for i, cn_name in enumerate(teachers, 1):
        print(f"[{i}/{len(teachers)}] ", end="")
        result = searcher.search_author(cn_name)
        all_results.append(result)
    
    print("-" * 60)
    
    # 3. 进行过滤和验证
    print(f"\n⏳ 进行机构过滤和拼音检验...\n")
    filtered_results = searcher.filter_and_verify(all_results)
    
    print("-" * 60)
    
    # 4. 保存 TARGETS
    saved_count = searcher.save_targets(filtered_results, OUTPUT_PATH)
    
    # 5. 输出统计信息
    print(f"\n📊 统计信息:")
    print(f"   处理老师数: {len(teachers)}")
    print(f"   有效 TARGETS 数: {saved_count}")
    
    # 统计每位老师的结果数
    print(f"\n📋 各老师的有效结果:")
    for cn_name in sorted(filtered_results.keys()):
        count = len(filtered_results[cn_name])
        if count > 0:
            print(f"   {cn_name}: {count} 条")
    
    print("\n✅ 程序完成！")
