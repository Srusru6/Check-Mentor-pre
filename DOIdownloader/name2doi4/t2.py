import time
import re
import requests # 导入新安装的requests库
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from webdriver_manager.chrome import ChromeDriverManager

def get_doi_from_crossref(title):
    """
    使用论文标题通过 CrossRef API 查询 DOI。
    这是一个独立的“侦探”函数。
    """
    base_api_url = "https://api.crossref.org/works"
    # 提供一个邮箱地址是使用CrossRef API的礼貌性要求
    headers = {'User-Agent': 'DOI-Finder-Script (mailto:your-email@example.com)'}
    params = {'query.bibliographic': title, 'rows': 1, 'sort': 'score'}
    try:
        response = requests.get(base_api_url, headers=headers, params=params, timeout=10)
        response.raise_for_status() # 如果请求失败则抛出异常
        data = response.json()
        if data['status'] == 'ok' and data['message']['items']:
            # 提取第一个、最匹配的结果的DOI
            return data['message']['items'][0].get('DOI')
    except requests.exceptions.RequestException as e:
        print(f"    [API请求错误] 查询时出错: {e}")
    except (KeyError, IndexError):
        # 如果返回的JSON结构不符合预期或为空
        print(f"    [API解析错误] 未能从返回结果中解析出DOI。")
    return None

def find_professor_papers(professor_name, institution):
    """
    为单个导师查找论文DOI的核心函数。
    策略: 搜姓名，用系所作为“加分项”，并对无DOI的论文进行API查询。
    """
    print("\n" + "="*50)
    print(f"开始处理: {professor_name} (机构优先项: {institution})")
    print("="*50)
    
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        options.binary_location = r"C:\otherapps\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(service=service, options=options)
        print("-> 驱动设置成功 (使用 webdriver-manager)！")
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

        # --- “加分项”决策逻辑 ---
        perfect_match_url, first_name_match_url = None, None
        for link_element in result_links[:3]:
            result_text = link_element.text
            if professor_name in result_text and institution in result_text:
                perfect_match_url = link_element.get_attribute("href")
                break
            if professor_name in result_text and not first_name_match_url:
                first_name_match_url = link_element.get_attribute("href")
        
        final_target_url = perfect_match_url or first_name_match_url
        if not final_target_url:
            print(f"-> 决策失败: 在前3个结果中未能找到任何与 '{professor_name}' 相关的导师。")
            driver.quit()
            return []
            
        print(f"  >> 最终导航至: {final_target_url}")
        driver.get(final_target_url)

        # --- 智能提取和查询DOI ---
        try:
            papers_article = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='近期论文']/parent::article")))
            papers_text_block = papers_article.find_element(By.CSS_SELECTOR, "p.tutor-display").text
            paper_lines = papers_text_block.strip().split('\n')
            print(f"-> 发现 {len(paper_lines)} 篇论文条目，开始逐一智能处理...")

            for i, line in enumerate(paper_lines):
                if not line.strip(): continue
                print(f"\n[处理第 {i+1} 篇]: {line[:80]}...")
                
                # 1. 优先尝试直接提取DOI
                doi_match = re.search(r'10\.\S+', line)
                if doi_match:
                    doi = re.sub(r'[\.,\)]$', '', doi_match.group(0))
                    print(f"  > 直接找到DOI: {doi}")
                    all_dois.append(doi)
                else:
                    # 2. 如果失败，则提取标题去API查询
                    print("  > 未直接找到DOI，尝试提取标题进行API查询...")
                    title_match = re.search(r'#\.\s(.*?)\.\s(Nature|Science|Optica|Light)', line)
                    if not title_match:
                         title_match = re.search(r'\d+\.\s(.*?)\.\s', line)

                    if title_match:
                        title = title_match.group(1).strip()
                        print(f"  > 提取到标题: '{title}'")
                        api_doi = get_doi_from_crossref(title)
                        if api_doi:
                            print(f"  > [API成功] 查找到DOI: {api_doi}")
                            all_dois.append(api_doi)
                        else:
                            print("  > [API失败] 未能通过标题查找到DOI。")
                        time.sleep(1) # 礼貌性等待，避免API请求过快
                    else:
                        print("  > 未能从此行提取出合适的标题用于查询。")
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
        with open(input_file, 'r', encoding='utf-8') as f: lines = f.readlines()
        if not lines:
            print(f"!!! 错误: '{input_file}' 文件是空的。"); return
            
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                prof_name, prof_inst = parts[0].strip(), parts[1].strip()
                if prof_name and prof_inst:
                    dois = find_professor_papers(prof_name, prof_inst)
                    all_results[f"{prof_name} ({prof_inst})"] = dois
        
        print("\n" + "*"*50 + "\n所有导师处理完毕，开始将结果写入文件...\n" + "*"*50)
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
        print(f"!!! 致命错误: 未找到输入文件 '{input_file}'。")
    except Exception as e:
        print(f"!!! 发生了一个未预料到的错误: {e}")

if __name__ == "__main__":
    main()