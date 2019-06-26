from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driverOptions = Options()
driverOptions.add_argument('--headless')
driverOptions.add_argument('--disable-gpu')


class page:
    def __init__(self, driver_options):
        self.cookies = []
        self.driver_options = driver_options

    def get(self, url):
        driver = webdriver.Chrome(options=self.driver_options)
        driver.get(url)
    
        if self.cookies:
            for cookie in self.cookies:
                driver.add_cookie(cookie)
        else:
            raw_cookies = driver.get_cookies()
            for cookie in raw_cookies:
                self.cookies.append({
                    'name': cookie['name'],
                    'value': cookie['value']
                })
        return driver


bilibili = page(driver_options=driverOptions)
b1 = bilibili.get('https://www.bilibili.com/')
b1.quit()
time.sleep(5)
b2 = bilibili.get('https://www.bilibili.com/')
b2.quit()
