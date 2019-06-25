import time
import threadpool
import chrome_action as action
import urllib
import socket
import os

# 多线程版本 
# nameList = ['mocha', 'quartz', 'asd']
# startTime = time.time()

# def sayHello (str):
#     # print ("hello", str)
#     time.sleep(2)

# # 实例化线程池
# pool = threadpool.ThreadPool(5)
# requests = threadpool.makeRequests(sayHello, nameList)

# for req in requests:
#     print('线程请求', req)
#     pool.putRequest(req)

# pool.wait()

# print ('%d second' % (time.time() - startTime)) 

def bilibili():

    def formatUrl(url):
        if url.find('//'):
            return url
        else:
            return "https:" + url

    def download_img (img):
        url = formatUrl(img.get('src'))
        alt = img.get('alt')
        if alt:
            url = url.split('.')
            #  去除尺寸参数
            url.pop(len(url) - 2)
            # 提取文件扩展名
            fileExt = url[len(url) - 1]
            fileName = './img/' + str(alt) + '.' + fileExt
            fileUrl = '.'.join(url)

            # 下载文件
            try:
                print(fileUrl)
                print(fileName)
                urllib.request.urlretrieve(fileUrl, fileName)
            except:
                print ('Network conditions is not good.')

    # 获取页面实例
    page = action.getPage('https://www.bilibili.com/')
    # 加载自定义 js 脚本
    action.load_script ('./js_script.js', page)
    # 等待 js 执行 完成
    time.sleep(20)
    # 获取页面源码
    pageSource = action.getPageSource(page)
    # 获取 img tags
    imgTags = action.get_img_tags(pageSource)
    # 下载 img tags 
    for img in imgTags:
        download_img(img)

bilibili()
