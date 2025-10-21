import time
import re
import requests
import random # 导入随机库
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from fake_useragent import UserAgent # 导入UserAgent库

def get_doi_from_crossref(title):
    # ... [此函数保持不变] ...
    # ...
    return None

def find_professor_papers(professor_name):
    """
    终极反反爬虫版: 集成了多种策略，模拟真实用户行为。
    """
    print("\n" + "="*50)
    print(f"开始处理: {professor_name}")
    print("="*50)
    
    driver = None
    try:
        options = uc.ChromeOptions()
        
        # --- 策略一: 基础伪装 ---
        # 1. 随机化User-Agent
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f'user-agent={user_agent}')
        print(f"-> 使用随机User-Agent: {user_agent}")
        
        # --- 策略二: 深度伪装 (加载用户数据，强烈推荐) ---
        # !! 使用前，请务必完全关闭您电脑上所有的Chrome浏览器 !!
        # 1. 在Chrome地址栏输入 chrome://version 找到“个人资料路径”
        # 2. 复制路径并替换下面的 placeholder
        user_data_path = r"C:\Users\您的用户名\AppData\Local\Google\Chrome\User Data"
        options.add_argument(f"--user-data-dir={user_data_path}")
        
        # --- 策略三: 终极手段 (使用代理，需要您自己提供代理地址) ---
        # 如果需要使用代理，请取消下面这行的注释，并替换为您自己的代理
        # proxy = "http://127.0.0.1:7890"  # 替换为您的HTTP或SOCKS5代理
        # options.add_argument(f'--proxy-server={proxy}')
        
        # 使用 undetected_chromedriver 启动
        driver = uc.Chrome(
            options=options,
            browser_executable_path=r"C:\otherapps\Google\Chrome\Application\chrome.exe",
            use_subprocess=True
        )
        print("-> 驱动设置成功 (undetected-chromedriver)！")

    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        print("!!! 请检查：1. 是否已关闭所有Chrome窗口？ 2. user_data_path是否正确？")
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
        
        # 模拟人类阅读时间
        time.sleep(random.uniform(2, 4))
        
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.teacher-search-btn")))
        search_button.click()
        
        result_list_css_selector = "div.teacher-search-list"
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, result_list_css_selector)))
        
        result_links = driver.find_elements(By.XPATH, f"//div[@class='teacher-search-list']/a")
        
        if not result_links:
            print(f"-> 未找到 '{professor_name}' 的任何搜索结果。")
            driver.quit()
            return []

        print(f"-> 找到 {len(result_links)} 个相关结果，将自动选择第一个。")
        first_result = result_links[0]
        final_target_url = first_result.get_attribute("href")
        
        # 模拟点击前的思考时间
        time.sleep(random.uniform(1, 3))
        
        print(f"  >> 自动选择第一个结果，导航至: {final_target_url}")
        driver.get(final_target_url)
        
        # 模拟加载和阅读教授主页的时间
        time.sleep(random.uniform(3, 5))

        # --- 在教授主页上提取DOI信息 ---
        try:
            papers_article = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h3[text()='近期论文']/parent::article"))
            )
            papers_text_block = papers_article.find_element(By.CSS_SELECTOR, "p.tutor-display").text
            paper_lines = papers_text_block.strip().split('\n')
            # ... [DOI提取和查询逻辑保持不变] ...
            for line in paper_lines:
                # ...
                all_dois.append("a_doi") # 示例
        
        except EC.TimeoutException:
            print("-> 警告: 在此页面上未找到‘近期论文’区域。")
        except Exception as e:
            print(f"-> 提取DOI时发生未知错误: {e}")

    except Exception as e:
        print(f"-> 处理 {professor_name} 时发生未知错误: {e}")
    finally:
        if driver:
            time.sleep(2) # 关闭前稍作停留
            driver.quit()

    unique_dois = list(set(all_dois))
    print(f"-> 完成处理: {professor_name}，找到 {len(unique_dois)} 个唯一DOI。")
    return unique_dois

def main():
    # ... [main 函数保持不变] ...
    # ...
    pass

if __name__ == "__main__":
    # 为了方便测试，您可以先只运行一个
    find_professor_papers("王剑威")
    # main() # 当您准备好批量运行时，再取消这行的注释