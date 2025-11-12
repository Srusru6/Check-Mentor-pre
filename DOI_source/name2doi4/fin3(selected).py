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

# --- 配置区域 ---
INSTITUTION_MAP = { "北京大学": "Peking University", "清华大学": "Tsinghua University" }

# --- 通用辅助函数 ---
def get_doi_from_openalex_api(work_id):
    if not work_id: return None
    try:
        response = requests.get(f"https://api.openalex.org/works/{work_id}", timeout=5)
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

# --- 引擎 1: OpenAlex (三步精确导航版) ---
def find_in_openalex(driver, wait, cn_name, cn_institution):
    print(f"  [OpenAlex] 正在搜索...")
    dois, profile_url = [], "未找到匹配主页"
    
    en_name = convert_name_to_openalex_format(cn_name)
    en_inst = INSTITUTION_MAP.get(cn_institution, cn_institution)
    
    try:
        # Step 1: 搜索并进入第一个作者的主页
        search_url = f"https://openalex.org/authors?page=1&filter=default.search:{en_name}"
        driver.get(search_url)
        
        first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.v-list-item")))
        profile_url = first_result.get_attribute("href")
        print(f"  [Step 1] 自动选择第一个结果，进入作者主页...")
        first_result.click()
        
        # Step 2: 在作者主页上，点击 "View works"
        wait.until(EC.url_contains("zoom=a"))
        try:
            view_works_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'works')]")
            ))
            print("  [Step 2] 找到 'View works' 按钮，点击进入成果列表...")
            view_works_button.click()
        except TimeoutException:
            print("  [Step 2] 未找到 'View works' 按钮，尝试直接构建URL...")
            author_id_match = re.search(r'zoom=(a\d+)', driver.current_url)
            if not author_id_match: return profile_url, []
            works_url = f"https://openalex.org/works?filter=authorships.author.id:{author_id_match.group(1)}"
            driver.get(works_url)

        # Step 3: 在成果列表页，点击机构筛选器
        wait.until(EC.url_contains("filter=authorships.author.id"))
        try:
            institution_filter_xpath = f"//td[normalize-space()='{en_inst}']"
            institution_filter = wait.until(EC.element_to_be_clickable((By.XPATH, institution_filter_xpath)))
            
            print(f"  [Step 3] 在成果页找到机构筛选器 '{en_inst}'，正在点击...")
            old_paper_list = driver.find_element(By.CSS_SELECTOR, "div.serp-results-list")
            institution_filter.click()
            wait.until(EC.staleness_of(old_paper_list))
            print("  [Step 3] 论文列表已根据机构筛选刷新。")
        except TimeoutException:
            print(f"  [Step 3] 在成果页右侧未找到机构筛选器 '{en_inst}'，将获取所有论文。")

        # Step 4: 翻页抓取
        print("  [Step 4] 开始翻页提取DOI...")
        page_num = 1
        while True:
            try:
                print(f"    - 正在处理第 {page_num} 页...")
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.serp-results-list a.v-list-item")))
                paper_items = driver.find_elements(By.CSS_SELECTOR, "div.serp-results-list a.v-list-item")
                if not paper_items and page_num == 1: break
                
                for paper in paper_items:
                    href = paper.get_attribute("href")
                    work_id_match = re.search(r'zoom=(w\d+)', href)
                    if work_id_match:
                        doi = get_doi_from_openalex_api(work_id_match.group(1))
                        if doi: dois.append(doi)
                        time.sleep(0.1)
                
                next_button = driver.find_element(By.CSS_SELECTOR, "li.v-pagination__next button")
                if "v-btn--disabled" in next_button.get_attribute("class"): break
                next_button.click()
                page_num += 1
                wait.until(EC.staleness_of(paper_items[0]))
                time.sleep(1)
            except (NoSuchElementException, TimeoutException): break
            
        return profile_url, dois
    except Exception as e:
        print(f"  [OpenAlex] 发生错误: {e}")
        return "查询出错", []

# --- 主程序 ---
def main():
    input_file = r"DOIdownloader\name2doi4\mnote.txt"
    output_file = r"DOIdownloader\results_openalex_only.txt"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f: lines = f.readlines()
        results_buffer = []
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                name, inst_cn = parts[0].strip(), parts[1].strip()
                print(f"\n>>> 正在处理: {name} ({inst_cn}) <<<")
                
                driver = init_driver()
                if not driver:
                    results_buffer.append(f"--- {name} ({inst_cn}) ---\n驱动初始化失败。\n\n")
                    continue
                wait = WebDriverWait(driver, 20)
                try:
                    profile_url, openalex_dois = find_in_openalex(driver, wait, name, inst_cn)
                    final_dois = sorted(list(set(openalex_dois)))
                    
                    res_str = f"--- {name} ({inst_cn}) ---\n"
                    res_str += f"OpenAlex Profile (selected): {profile_url}\n"
                    res_str += f"Found DOIs ({len(final_dois)}):\n"
                    res_str += "".join(f"{i}. {doi}\n" for i, doi in enumerate(final_dois, 1)) if final_dois else "无 DOI 记录\n"
                    res_str += "\n"
                    results_buffer.append(res_str)
                    print(f">>> {name} 处理完毕。")
                finally:
                    if driver: driver.quit()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(results_buffer)
        print(f"\n*** 全部完成！结果已保存至: {output_file} ***")
    except FileNotFoundError:
        print(f"!!! 未找到输入文件: {input_file}")

if __name__ == "__main__":
    main()