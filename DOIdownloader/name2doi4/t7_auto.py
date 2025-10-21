import time
import re
import requests
import configparser # 导入用于读取配置文件的库
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from fake_useragent import UserAgent

def get_doi_from_crossref(title):
    # ... [此函数保持不变] ...
    return None

def login_to_xmol(driver, wait, username, password):
    """
    一个专门用于登录X-MOL的函数。
    """
    try:
        login_url = "https://www.x-mol.com/login"
        print(f"-> 正在导航到登录页面: {login_url}")
        driver.get(login_url)
        
        # 定位用户名和密码输入框，并输入信息
        # 根据X-MOL登录页的HTML结构，输入框的name属性是'username'和'password'
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        
        print("-> 找到输入框，正在输入用户名和密码...")
        username_input.send_keys(username)
        password_input.send_keys(password)
        
        # 定位并点击登录按钮
        # 按钮的文本是“登录”，我们可以用XPath来定位
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '登录')]")))
        login_button.click()
        
        # 等待登录成功的标志
        # 一个好的标志是等待右上角的用户名出现，它通常在一个class为'user-name'的元素里
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.user-name")))
        print("-> 登录成功！")
        return True
        
    except Exception as e:
        print(f"!!! 登录失败: {e}")
        return False

def find_professor_papers(professor_name, username, password):
    """
    具备自动登录功能的版本。
    """
    print("\n" + "="*50)
    print(f"开始处理: {professor_name}")
    print("="*50)
    
    driver = None
    try:
        options = uc.ChromeOptions()
        ua = UserAgent()
        options.add_argument(f'user-agent={ua.random}')
        
        driver = uc.Chrome(
            options=options,
            browser_executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            use_subprocess=True
        )
        print("-> 驱动设置成功 (undetected-chromedriver)！")

    except Exception as e:
        print(f"!!! 驱动初始化失败: {e}")
        if driver: driver.quit()
        return []

    all_dois = []
    wait = WebDriverWait(driver, 20)
    
    # --- 核心修改：在所有操作之前，先执行登录 ---
    if not login_to_xmol(driver, wait, username, password):
        # 如果登录失败，则没有必要继续
        if driver: driver.quit()
        return []
    
    # 登录成功后，等待一下，让页面稳定
    time.sleep(2)

    try:
        # --- 后续的搜索和爬取逻辑保持不变 ---
        base_url = "https://www.x-mol.com/university/searchTutor/simple?option="
        encoded_query = quote(professor_name)
        target_url = base_url + encoded_query
        print(f"-> 正在搜索姓名: '{professor_name}'")
        driver.get(target_url)
        
        # ... [后续的所有搜索、选择、提取DOI的逻辑都保持不变] ...
        
    except Exception as e:
        print(f"-> 处理 {professor_name} 时发生未知错误: {e}")
    finally:
        if driver:
            time.sleep(2)
            driver.quit()

    unique_dois = list(set(all_dois))
    print(f"-> 完成处理: {professor_name}，找到 {len(unique_dois)} 个唯一DOI。")
    return unique_dois

def main():
    """
    主函数，读取配置文件和mnote.txt，然后批量处理。
    """
    # --- 核心修改：从 config.ini 读取用户名和密码 ---
    config = configparser.ConfigParser()
    try:
        config.read('config.ini', encoding='utf-8')
        username = config['credentials']['username']
        password = config['credentials']['password']
        if not username or not password:
            raise KeyError
    except (KeyError, FileNotFoundError):
        print("!!! 致命错误: 'config.ini' 文件未找到或内容不正确。")
        print("!!! 请确保在项目目录下创建了 config.ini 文件，并包含以下内容:")
        print("[credentials]\nusername = your_username\npassword = your_password")
        return
    
    input_file = r"DOIdownloader\name2doi4\mnote.txt"
    output_file = r"DOIdownloader\results.txt"
    all_results = {}

    try:
        with open(input_file, 'r', encoding='utf-8') as f: lines = f.readlines()
        if not lines:
            print(f"!!! 错误: '{input_file}' 文件是空的。"); return
            
        for line in lines:
            parts = line.strip().split('\t')
            if parts:
                prof_name = parts[0].strip()
                if prof_name:
                    # 将用户名和密码传递给核心函数
                    dois = find_professor_papers(prof_name, username, password)
                    all_results[prof_name] = dois
        
        # ... [写入文件的逻辑保持不变] ...
        
    except FileNotFoundError:
        print(f"!!! 致命错误: 未找到输入文件 '{input_file}'。")
    except Exception as e:
        print(f"!!! 发生了一个未预料到的错误: {e}")

if __name__ == "__main__":
    main()