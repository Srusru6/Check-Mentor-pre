import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urllib.parse import quote
from webdriver_manager.chrome import ChromeDriverManager
from pypinyin import pinyin, Style

# --- 配置区域 & 通用辅助函数 [保持不变] ---
INSTITUTION_MAP = {
    "北京大学": "Peking University",
    "清华大学": "Tsinghua University",
}

def get_doi_from_openalex_api(work_id):
    if not work_id: return None
    api_url = f"https://api.openalex.org/works/{work_id}"
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            doi_url = response.json().get('doi')
            if doi_url: return doi_url.replace("https://doi.org/", "")
    except: pass
    return None

def convert_name_to_openalex_format(name):
    if not name: return ""
    p_list = pinyin(name, style=Style.NORMAL)
    if len(p_list) < 2: return name.capitalize()
    last_name = p_list[0][0].capitalize()
    first_name = "".join([item[0] for item in p_list[1:]]).capitalize()
    return f"{first_name}+{last_name}"

def init_driver():
    try:
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        options.binary_location = r"C:\otherapps\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(service=service, options=options)
        print("-> 驱动设置成功 (使用 webdriver-manager)！")
        return driver
    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        return None

# --- OpenAlex 查询引擎 (修改为生成器) ---
def find_in_openalex(driver, wait, cn_name, cn_institution):
    """
    在 OpenAlex 上查找导师，并以生成器的方式逐个产生 DOI。
    """
    print(f"  [OpenAlex] 正在搜索...")
    en_name = convert_name_to_openalex_format(cn_name)
    en_inst = INSTITUTION_MAP.get(cn_institution, cn_institution)
    
    try:
        search_url = f"https://openalex.org/authors?page=1&filter=default.search:{en_name}"
        driver.get(search_url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.v-list-item")))
        
        found_author = False
        for item in driver.find_elements(By.CSS_SELECTOR, "a.v-list-item")[:5]:
            if en_inst.lower() in item.text.lower():
                print(f"  [OpenAlex] 找到匹配机构 '{en_inst}'，点击进入主页...")
                item.click()
                found_author = True
                break
        
        if not found_author:
            print(f"  [OpenAlex] 在前5个结果中未找到机构为 '{en_inst}' 的匹配项。")
            return

        wait.until(EC.url_contains("zoom=a"))
        author_id_match = re.search(r'zoom=(a\d+)', driver.current_url)
        if not author_id_match:
            return
            
        author_id = author_id_match.group(1)
        works_url = f"https://openalex.org/works?filter=authorships.author.id:{author_id}"
        print(f"  [OpenAlex] 导航至Works页面: {works_url}")
        driver.get(works_url)

        page_num = 1
        while True:
            print(f"  [OpenAlex] 正在处理论文列表第 {page_num} 页...")
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.serp-results-list a.v-list-item")))
            paper_items = driver.find_elements(By.CSS_SELECTOR, "div.serp-results-list a.v-list-item")
            
            for paper in paper_items:
                href = paper.get_attribute("href")
                work_id_match = re.search(r'zoom=(w\d+)', href)
                if work_id_match:
                    doi = get_doi_from_openalex_api(work_id_match.group(1))
                    if doi:
                        # --- 核心修改：使用 yield “吐出” DOI ---
                        yield doi
                    time.sleep(0.1)

            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.v-pagination__next button")
                if "v-btn--disabled" in next_button.get_attribute("class"):
                    print("  [OpenAlex] 到达最后一页，翻页结束。")
                    break
                else:
                    print("  [OpenAlex] 点击下一页...")
                    next_button.click()
                    page_num += 1
                    wait.until(EC.staleness_of(paper_items[0]))
                    time.sleep(1)
            except NoSuchElementException:
                print("  [OpenAlex] 未找到下一页按钮，翻页结束。")
                break
    except Exception as e:
        print(f"  [OpenAlex] 发生错误: {e}")

# --- 主程序 (重构为实时写入) ---
def main():
    input_file = r"DOIdownloader\name2doi4\mnote.txt"
    output_file = r"DOIdownloader\results_openalex_realtime.txt"
    CHUNK_SIZE = 10 # 每10篇写入一次
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f: lines = f.readlines()
        
        # --- 核心修改：在循环外打开文件 ---
        with open(output_file, 'w', encoding='utf-8') as f_out:
            print(f"--- 准备开始处理 {len(lines)} 位导师，结果将实时写入 {output_file} ---")

            for line in lines:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    name, inst_cn = parts[0].strip(), parts[1].strip()
                    print(f"\n>>> 正在处理: {name} ({inst_cn}) <<<")
                    
                    # 写入导师标题
                    f_out.write(f"--- {name} ({inst_cn}) ---\n")
                    
                    driver = init_driver()
                    if not driver:
                        f_out.write("驱动初始化失败，跳过。\n\n")
                        continue
                    
                    wait = WebDriverWait(driver, 20)
                    
                    # --- 核心修改：实时处理与写入 ---
                    chunk = []
                    seen_dois = set()
                    total_found = 0
                    
                    try:
                        # 遍历生成器产出的每一个DOI
                        for doi in find_in_openalex(driver, wait, name, inst_cn):
                            if doi not in seen_dois:
                                seen_dois.add(doi)
                                chunk.append(doi)
                                total_found += 1
                                
                                # 如果缓冲区满了，就写入文件
                                if len(chunk) >= CHUNK_SIZE:
                                    print(f"  >> 达到 {CHUNK_SIZE} 篇，正在写入文件...")
                                    for d in sorted(chunk):
                                        f_out.write(f"{d}\n")
                                    f_out.flush() # 强制将内容写入磁盘
                                    chunk = [] # 清空缓冲区
                        
                        # 处理完一个导师后，写入剩余的DOI
                        if chunk:
                            print(f"  >> 正在写入剩余的 {len(chunk)} 篇...")
                            for d in sorted(chunk):
                                f_out.write(f"{d}\n")
                            chunk = []
                            
                        if total_found == 0:
                            f_out.write("无 DOI 记录\n")
                            
                        f_out.write("\n")
                        f_out.flush()
                        print(f">>> {name} 处理完毕，共找到 {total_found} 个唯一DOI。")

                    finally:
                        if driver: driver.quit()

        print(f"\n*** 全部完成！***")

    except FileNotFoundError:
        print(f"!!! 未找到输入文件: {input_file}")

if __name__ == "__main__":
    main()