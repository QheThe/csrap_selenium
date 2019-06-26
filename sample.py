from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driverOptions = Options()
# driverOptions.add_argument('--headless')
# driverOptions.add_argument('--disable-gpu')


class page:
    def __init__(self, driver_options):
        self.cookies = []
        self.driver_options = driver_options

    def open(self, url, cookie_chache_wait):
        driver = webdriver.Chrome(options=self.driver_options)
        driver.get(url)

        if self.cookies:
            for cookie in self.cookies:
                driver.add_cookie(cookie)
            time.sleep(1)
            driver.refresh()
            print('cookie 恢复 浏览器刷新')
                
        raw_cookies = driver.get_cookies()
        time.sleep(cookie_chache_wait)
        for cookie in raw_cookies:
            self.cookies.append({
                'name': cookie['name'],
                'value': cookie['value']
            })
        for cookie in self.cookies:
            print('缓存 cookie')
            print(cookie)
        return driver

bilibili = page(driver_options=driverOptions)
b1 = bilibili.open(url='https://www.bilibili.com', cookie_chache_wait=20)
b1.quit()

time.sleep(2)

b2 = bilibili.open(url='https://www.bilibili.com', cookie_chache_wait=50)
b2.quit()