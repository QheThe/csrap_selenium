from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import lxml

driver_options = Options()
# driver_options.add_argument('--headless')
# driver_options.add_argument('--disable-gpu')

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

def getPageSource(url):
    page = getPage(url)
    # 对付懒加载
    js="window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)
    return page.page_source

def get_pic(url):
    rawPageSource = getPageSource(url)

    parsedHtml = BeautifulSoup(rawPageSource, 'lxml')
    imgTags = parsedHtml.find_all('img')
    return imgTags