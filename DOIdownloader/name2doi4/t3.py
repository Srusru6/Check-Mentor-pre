import time
import re
import requests # 导入新安装的requests库
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

    Args:
        title (str): 论文的标题。

    Returns:
        str: 找到的DOI号，如果找不到则返回 None。
    """
    base_api_url = "https://api.crossref.org/works"
    # 我们提供一个邮箱地址，这是使用CrossRef API的礼貌性要求
    headers = {
        'User-Agent': 'DOI-Finder-Script (mailto:your-email@example.com)'
    }
    # 构建查询参数，按相关性排序，只取第一个结果
    params = {
        'query.bibliographic': title,
        'rows': 1,
        'sort': 'score'
    }
    
    try:
        response = requests.get(base_api_url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # 如果请求失败 (如 404, 500)，则会抛出异常
        
        data = response.json()
        if data['status'] == 'ok' and data['message']['items']:
            # 提取第一个结果的DOI
            doi = data['message']['items'][0].get('DOI')
            return doi
    except requests.exceptions.RequestException as e:
        print(f"    [API请求错误] 查询 '{title[:30]}...' 时出错: {e}")
    except (KeyError, IndexError):
        # 如果返回的JSON结构不符合预期
        print(f"    [API解析错误] 未能从 '{title[:30]}...' 的返回结果中解析出DOI。")
        
    return None

def find_professor_papers(professor_name, institution):
    """
    最终智能版: 抓取论文列表，对没有DOI的条目，使用CrossRef API进行查询。
    """
    # ... [启动浏览器的代码保持不变] ...
    print("正在设置 Google Chrome 浏览器驱动...")
    try:
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        options.binary_location = r"C:\otherapps\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(service=service, options=options)
        print("驱动设置成功！")
    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        return []

    all_dois = []
    wait = WebDriverWait(driver, 20)
    
    try:
        # ... [搜索和导航到教授主页的代码保持不变] ...
        base_url = "https://www.x-mol.com/university/searchTutor/simple?option="
        search_query = f"{professor_name} {institution}"
        encoded_query = quote(search_query)
        target_url = base_url + encoded_query
        driver.get(target_url)
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.teacher-search-btn")))
        search_button.click()
        result_list_css_selector = "div.teacher-search-list"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, result_list_css_selector)))
        result_links = driver.find_elements(By.XPATH, f"//div[@class='teacher-search-list']/a")
        found_professor_flag = False
        for link_element in result_links[:3]:
            result_text = link_element.text
            if professor_name in result_text and institution in result_text:
                target_url = link_element.get_attribute("href")
                driver.get(target_url)
                found_professor_flag = True
                break
        if not found_professor_flag:
            print("未找到匹配的教授主页")
            return []

        # --- 核心修改：智能提取和查询DOI ---
        print(f"\n已成功导航到 {professor_name} 的个人主页，准备提取论文信息...")
        try:
            papers_article = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h3[text()='近期论文']/parent::article"))
            )
            papers_text_block = papers_article.find_element(By.CSS_SELECTOR, "p.tutor-display").text
            
            # 将整个文本块按行分割成一个论文列表
            paper_lines = papers_text_block.strip().split('\n')
            print(f"--- 发现 {len(paper_lines)} 篇论文条目，开始逐一处理 ---")

            for i, line in enumerate(paper_lines):
                if not line.strip(): continue # 跳过空行

                print(f"\n[处理第 {i+1} 篇]: {line[:80]}...")
                
                # 1. 首先尝试直接从文本中匹配DOI
                doi_match = re.search(r'10\.\S+', line)
                if doi_match:
                    doi = re.sub(r'[\.,\)]$', '', doi_match.group(0))
                    print(f"  > 直接找到DOI: {doi}")
                    all_dois.append(doi)
                else:
                    # 2. 如果找不到，则提取标题去API查询
                    print("  > 未直接找到DOI，尝试提取标题进行API查询...")
                    # 提取标题的一个简单方法：假设标题在 " Wang#." 或类似作者列表之后，直到期刊名（如 "Nature"）之前
                    # 这是一个启发式规则，可能需要根据实际情况微调
                    # 我们从 ". " 后面开始，到句号或问号结束，作为标题
                    title_match = re.search(r'#\.\s(.*?)\.\s(Nature|Science|Optica|Light)', line)
                    if not title_match:
                         title_match = re.search(r'\d+\.\s(.*?)\.\s', line) # 尝试更通用的匹配

                    if title_match:
                        title = title_match.group(1)
                        print(f"  > 提取到标题: '{title}'")
                        
                        # 调用API函数查询
                        api_doi = get_doi_from_crossref(title)
                        
                        if api_doi:
                            print(f"  > [API成功] 查找到DOI: {api_doi}")
                            all_dois.append(api_doi)
                        else:
                            print("  > [API失败] 未能通过标题查找到DOI。")
                        
                        time.sleep(1) # 礼貌性等待，避免请求过于频繁
                    else:
                        print("  > 未能从此行提取出合适的标题。")

        except Exception as e:
            print(f"!!! 提取DOI时发生错误: {e}")

    except Exception as e:
        print(f"!!! 发生未知错误: {e}")
    finally:
        print("\n任务完成，关闭浏览器。")
        driver.quit()

    return all_dois

if __name__ == "__main__":
    PROFESSOR_NAME = "王剑威"
    INSTITUTION = "北京大学"
    found_dois = find_professor_papers(PROFESSOR_NAME, INSTITUTION)

    if found_dois:
        print(f"\n--- 最终找到 {PROFESSOR_NAME} 老师的 {len(found_dois)} 个 DOI ---")
        # 使用set去重后打印
        unique_dois = sorted(list(set(found_dois)))
        print(f"--- (去重后共 {len(unique_dois)} 个) ---")
        for i, doi in enumerate(unique_dois, 1):
            print(f"{i}. {doi}")
        print("------------------------------------------")
    else:
        print(f"\n未能获取到 {PROFESSOR_NAME} 老师的任何论文 DOI。")