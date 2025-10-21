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
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote

def get_doi_from_crossref(title):
    """
    使用论文标题通过 CrossRef API 查询 DOI。
    """
    base_api_url = "https://api.crossref.org/works"
    headers = {'User-Agent': 'DOI-Finder-Script (mailto:your-email@example.com)'}
    params = {'query.bibliographic': title, 'rows': 1, 'sort': 'score'}
    try:
        response = requests.get(base_api_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'ok' and data['message']['items']:
            return data['message']['items'][0].get('DOI')
    except requests.exceptions.RequestException as e:
        print(f"    [API请求错误] 查询时出错: {e}")
    except (KeyError, IndexError):
        print(f"    [API解析错误] 未能解析出DOI。")
    return None

def find_professor_papers(professor_name):
    """
    为单个导师查找论文DOI的核心函数。
    策略: 仅用姓名搜索，并自动选择第一个结果。
    """
    print("\n" + "="*50)
    print(f"开始处理: {professor_name}")
    print("="*50)
    
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        options.binary_location = r"C:\otherapps\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        if driver: driver.quit()
        return []

    all_dois = []
    wait = WebDriverWait(driver, 20)
    
    try:
        base_url = "https://www.x-mol.com/university/searchTutor/simple?option="
        encoded_query = quote(professor_name)
        target_url = base_url + encoded_query
        print(f"-> 正在搜索姓名: '{professor_name}'")
        driver.get(target_url)
        
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.teacher-search-btn")))
        search_button.click()
        
        result_list_css_selector = "div.teacher-search-list"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, result_list_css_selector)))
        
        result_links = driver.find_elements(By.XPATH, f"//div[@class='teacher-search-list']/a")
        
        if not result_links:
            print(f"-> 未找到 '{professor_name}' 的任何搜索结果。")
            driver.quit()
            return []

        # --- 核心修改：不再验证，直接选择第一个结果 ---
        print(f"-> 找到 {len(result_links)} 个相关结果，将自动选择第一个。")
        first_result = result_links[0]
        target_url = first_result.get_attribute("href")
        print(f"  >> 自动选择第一个结果，导航至: {target_url}")
        driver.get(target_url)

        # --- 提取和查询DOI ---
        try:
            papers_article = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h3[text()='近期论文']/parent::article"))
            )
            papers_text_block = papers_article.find_element(By.CSS_SELECTOR, "p.tutor-display").text
            paper_lines = papers_text_block.strip().split('\n')

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
            driver.quit()

    unique_dois = list(set(all_dois))
    print(f"-> 完成处理: {professor_name}，找到 {len(unique_dois)} 个唯一DOI。")
    return unique_dois

def main():
    """
    主函数，读取mnote.txt并批量处理导师。
    """
    input_file = r"DOIdownloader\name2doi4\mnote.txt"
    output_file = r"DOIdownloader\results.txt"
    all_results = {}

    try:
        print(f"--- 开始读取导师列表文件: {input_file} ---")
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines:
            print(f"!!! 错误: '{input_file}' 文件是空的。")
            return
            
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line: continue

            # --- 核心修改：只读取姓名 ---
            # 假设文件格式仍然是“姓名\t系所”，我们只取第一部分
            parts = line.split('\t')
            if parts:
                prof_name = parts[0].strip()
                if prof_name:
                    # 调用只接收一个参数的核心函数
                    dois = find_professor_papers(prof_name)
                    all_results[prof_name] = dois
            else:
                print(f"!!! 警告: 第 {line_num} 行格式错误，已跳过: '{line}'")
        
        print("\n" + "*"*50)
        print("所有导师处理完毕，开始将结果写入文件...")
        print("*"*50)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for professor, dois in all_results.items():
                f.write(f"--- {professor} ---\n")
                if dois:
                    for i, doi in enumerate(sorted(dois), 1):
                        f.write(f"{i}. {doi}\n")
                else:
                    f.write("未能获取到任何DOI。\n")
                f.write("\n")
        
        print(f"成功！所有结果已保存到 '{output_file}' 文件中。")

    except FileNotFoundError:
        print(f"!!! 致命错误: 未找到输入文件 '{input_file}'。请在脚本同目录下创建它。")
    except Exception as e:
        print(f"!!! 发生了一个未预料到的错误: {e}")


if __name__ == "__main__":
    main()