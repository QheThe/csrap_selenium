from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import lxml

driver_options = Options()
driver_options.add_argument('--headless')
driver_options.add_argument('--disable-gpu')
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
driver_options.add_argument('user-agent=' + ua)

def waitForElLoadByTagName (tagName, wait, browser):
    waiter = WebDriverWait(driver=browser, timeout=wait, poll_frequency=0.5)
    waiter.until(EC.presence_of_element_located((By.TAG_NAME, tagName)))

def getPage (url):
    # 实例化 webdriver
    driver = webdriver.Chrome(options=driver_options)
    # 获取页面
    driver.get(url)
    # 将页面实例返回
    return driver

def getPageSource(page):
    pageSource = page.page_source
    page.quit()
    return pageSource 

def load_script(script_path, driver):
    fp = open(script_path, "r")
    driver.execute_script(fp.read())

def get_img_tags(pageSource):
    parsedHtml = BeautifulSoup(pageSource, 'lxml')
    imgTags = parsedHtml.find_all('img')
    return imgTags