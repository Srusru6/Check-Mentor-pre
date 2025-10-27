import time
import re # 导入正则表达式库
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote

def find_professor_papers(professor_name, institution):
    """
    最终完整版: 完成所有步骤，包括搜索、导航、并从主页的论文文本中提取DOI。
    """
    # --- 1. 启动Google Chrome浏览器 ---
    print("正在设置 Google Chrome 浏览器驱动...")
    try:
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--start-maximized")
        # 确保这里的路径是您电脑上 chrome.exe 的实际路径
        options.binary_location = r"C:\otherapps\Google\Chrome\Application\chrome.exe"
        driver = webdriver.Chrome(service=service, options=options)
        print("驱动设置成功！")
    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        return []

    dois = []
    wait = WebDriverWait(driver, 20)
    
    try:
        # --- 2. 访问页面并触发搜索 ---
        base_url = "https://www.x-mol.com/university/searchTutor/simple?option="
        search_query = f"{professor_name} {institution}"
        encoded_query = quote(search_query)
        target_url = base_url + encoded_query
        
        print(f"直接访问预填好搜索词的页面: {target_url}")
        driver.get(target_url)
        print("页面加载成功，搜索词已由URL自动填入。")
        
        search_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.teacher-search-btn"))
        )
        search_button.click()
        print("已点击搜索按钮，等待结果加载...")

        # --- 3. 解析结果并直接导航 ---
        result_list_css_selector = "div.teacher-search-list"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, result_list_css_selector)))
        print("搜索结果列表已加载。")

        result_links = driver.find_elements(By.XPATH, f"//div[@class='teacher-search-list']/a")
        
        if not result_links:
            print("!!! 错误: 搜索结果列表中未找到任何导师链接。")
            return []

        print(f"共找到 {len(result_links)} 个结果，将进行检查...")
        
        found_professor_flag = False
        for index, link_element in enumerate(result_links[:3]):
            result_text = link_element.text
            if professor_name in result_text and institution in result_text:
                print(f"*** 找到完全匹配的结果 (结果 {index + 1})，执行导航 ***")
                target_url = link_element.get_attribute("href")
                print(f"获取到主页URL，直接导航至: {target_url}")
                driver.get(target_url)
                found_professor_flag = True
                break
        
        if not found_professor_flag:
            print(f"!!! 错误: 在前3个结果中未能找到 '{professor_name} ({institution})' 的主页。")
            return []

        # --- 4. 在教授主页上提取DOI信息 ---
        print(f"已成功导航到 {professor_name} 的个人主页。")

        # 【核心修改】定位论文区域并提取DOI
        try:
            # 1. 使用XPath定位到“近期论文”所在的<article>标签
            #    这个XPath的意思是：找到一个<h3>标签，其文本是“近期论文”，然后选择它的父级<article>标签
            papers_article = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h3[text()='近期论文']/parent::article"))
            )
            
            # 2. 从这个<article>中获取包含所有论文的<p>标签的文本
            papers_text_block = papers_article.find_element(By.CSS_SELECTOR, "p.tutor-display").text
            print("\n--- 成功提取到论文文本块 ---")
            
            # 3. 使用正则表达式查找所有DOI号
            #    这个正则表达式匹配 "10." 开头，后面跟着数字、点、斜杠、括号、字母等字符，直到遇到空格或换行
            doi_pattern = r'10\.\S+'
            found_dois = re.findall(doi_pattern, papers_text_block)
            
            # 清理可能包含在DOI末尾的标点符号
            for doi in found_dois:
                # 移除末尾可能存在的句号、逗号或右括号
                cleaned_doi = re.sub(r'[\.,\)]$', '', doi)
                dois.append(cleaned_doi)

            print(f"--- 从文本中成功解析出 {len(dois)} 个DOI ---")
            
        except TimeoutException:
            print("!!! 警告: 在页面上未找到“近期论文”区域。")
        except Exception as e:
            print(f"!!! 提取DOI时发生错误: {e}")

    except TimeoutException:
        print(f"!!! 操作超时。请检查网络或确认网站 '{driver.current_url}' 的元素选择器是否仍然有效。")
    except Exception as e:
        print(f"!!! 发生未知错误: {e}")
    finally:
        print("\n任务完成，关闭浏览器。")
        driver.quit()

    return dois

if __name__ == "__main__":
    PROFESSOR_NAME = "王剑威"
    INSTITUTION = "北京大学"
    found_dois = find_professor_papers(PROFESSOR_NAME, INSTITUTION)

    if found_dois:
        print(f"\n--- 最终找到 {PROFESSOR_NAME} 老师的 {len(found_dois)} 个 DOI ---")
        for i, doi in enumerate(found_dois, 1):
            print(f"{i}. {doi}")
        print("------------------------------------------")
    else:
        print(f"\n未能获取到 {PROFESSOR_NAME} 老师的任何论文 DOI。")