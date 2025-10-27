import time
import re
import requests
# 核心修改：导入 undetected_chromedriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote

# ... [get_doi_from_crossref 函数保持不变] ...
def get_doi_from_crossref(title):
    base_api_url = "https://api.crossref.org/works"
    headers = {'User-Agent': 'DOI-Finder-Script (mailto:2400011484@stu.pku.edu.cn)'}
    params = {'query.bibliographic': title, 'rows': 1, 'sort': 'score'}
    try:
        response = requests.get(base_api_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'ok' and data['message']['items']:
            return data['message']['items'][0].get('DOI')
    except:
        return None

def find_professor_papers(professor_name, institution):
    """
    反反爬虫优化版:
    1. 使用 undetected_chromedriver 隐藏机器人特征。
    2. 加载本地Chrome用户数据，以保持登录状态 (Cookies)。
    3. 加入随机延时，模拟人类行为。
    """
    print("\n" + "="*50)
    print(f"开始处理: {professor_name} ({institution})")
    print("="*50)
    
    driver = None
    try:
        # --- 反反爬虫优化 1: 初始化 undetected_chromedriver ---
        options = uc.ChromeOptions()
        
        # --- 反反爬虫优化 2: 加载您的Chrome用户数据 ---
        # 请确保已完全关闭所有Chrome窗口，并将下面的路径替换为您自己的
        user_data_path = r"C:\Users\您的用户名\AppData\Local\Google\Chrome\User Data"
        options.add_argument(f"--user-data-dir={user_data_path}")
        
        # 我们不再需要手动指定 binary_location，uc 会自动寻找
        # options.binary_location = r"C:\otherapps\Google\Chrome\Application\chrome.exe"
        
        # 使用 uc.Chrome 启动浏览器
        driver = uc.Chrome(options=options, use_subprocess=True)
        print("-> 驱动设置成功 (undetected-chromedriver)！")

    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        print("!!! 请确保：1. 已完全关闭所有Chrome窗口。 2. user_data_path路径正确。")
        if driver: driver.quit()
        return []

    all_dois = []
    wait = WebDriverWait(driver, 20)
    
    try:
        base_url = "https://www.x-mol.com/university/searchTutor/simple?option="
        encoded_query = quote(professor_name)
        target_url = base_url + encoded_query
        print(f"-> 正在搜索姓名: '{professor_name}' (稍后将用 '{institution}' 进行验证)")
        driver.get(target_url)
        
        # --- 反反爬虫优化 3: 加入随机延时 ---
        time.sleep(2) # 模拟打开页面后看一眼的时间

        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.teacher-search-btn")))
        search_button.click()
        
        result_list_css_selector = "div.teacher-search-list"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, result_list_css_selector)))
        
        time.sleep(1) # 模拟看完搜索结果列表

        result_links = driver.find_elements(By.XPATH, f"//div[@class='teacher-search-list']/a")
        
        if not result_links:
            print(f"-> 未找到 '{professor_name}' 的任何搜索结果。")
            driver.quit()
            return []

        print(f"-> 找到 {len(result_links)} 个相关结果，开始验证前3个...")
        found_professor_flag = False
        for index, link_element in enumerate(result_links[:3]):
            result_text = link_element.text
            if professor_name in result_text and institution in result_text:
                target_url = link_element.get_attribute("href")
                print(f"  >> 成功匹配! 导航至: {target_url}")
                driver.get(target_url)
                found_professor_flag = True
                break
        
        if not found_professor_flag:
            print(f"-> 在前3个结果中未找到同时匹配 '{professor_name}' 和 '{institution}' 的主页。")
            driver.quit()
            return []
        
        time.sleep(3) # 模拟阅读教授主页

        # --- 提取和查询DOI ---
        try:
            papers_article = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h3[text()='近期论文']/parent::article"))
            )
            papers_text_block = papers_article.find_element(By.CSS_SELECTOR, "p.tutor-display").text
            paper_lines = papers_text_block.strip().split('\n')
            # ... [后续DOI提取逻辑不变] ...
            for line in paper_lines:
                if not line.strip(): continue
                
                doi_match = re.search(r'10\.\S+', line)
                if doi_match:
                    doi = re.sub(r'[\.,\)]$', '', doi_match.group(0))
                    all_dois.append(doi)
                else:
                    title_match = re.search(r'#\.\s(.*?)\.\s(Nature|Science|Optica|Light)', line)
                    if not title_match:
                         title_match = re.search(r'\d+\.\s(.*?)\.\s', line)

                    if title_match:
                        title = title_match.group(1)
                        api_doi = get_doi_from_crossref(title)
                        if api_doi:
                            all_dois.append(api_doi)
                        time.sleep(0.5)

        except Exception as e:
            print(f"-> 提取DOI时发生错误: {e}")

    except Exception as e:
        print(f"-> 处理 {professor_name} 时发生未知错误: {e}")
    finally:
        if driver:
            # 加上一个等待，让您有机会看到最后的操作
            time.sleep(2)
            driver.quit()

    unique_dois = list(set(all_dois))
    print(f"-> 完成处理: {professor_name}，找到 {len(unique_dois)} 个唯一DOI。")
    return unique_dois

# ... [main 函数保持不变] ...
def main():
    input_file = r"DOIdownloader\name2doi4\mnote.txt"
    output_file = r"DOIdownloader\results.txt"
    all_results = {}
    try:
        with open(input_file, 'r', encoding='utf-8') as f: lines = f.readlines()
        if not lines:
            print(f"'{input_file}' is empty."); return
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                prof_name, prof_inst = parts[0].strip(), parts[1].strip()
                all_results[f"{prof_name} ({prof_inst})"] = find_professor_papers(prof_name, prof_inst)
        with open(output_file, 'w', encoding='utf-8') as f:
            for professor, dois in all_results.items():
                f.write(f"--- {professor} ---\n")
                f.write("未能获取到任何DOI。\n" if not dois else "".join(f"{i}. {doi}\n" for i, doi in enumerate(sorted(dois), 1)))
                f.write("\n")
        print(f"\nSuccess! All results saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"!!! Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"!!! An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()