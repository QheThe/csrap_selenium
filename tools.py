import time
import threadpool
from bs4 import BeautifulSoup
import lxml
import urllib

def parseHtml(pageSource):
    return BeautifulSoup(pageSource, 'lxml')

def get_img_tags(pageSource):
    parsedHtml = parseHtml(pageSource)
    imgTags = parsedHtml.find_all('img')
    return imgTags

def download_file(url, fileName):
    # 提取文件扩展名
    fileExt = url[len(url) - 1]
    fileName = fileName + '.' + fileExt
    fileUrl = '.'.join(url)
    # 下载文件
    try:
        print(fileUrl)
        print(fileName)
        urllib.request.urlretrieve(fileUrl, fileName)
    except:
        print ('Network conditions is not good.')

class createMultiThread:
    def __init__(self, threadNum, threadReqFunc, threadReqList, threadCreating, threadDone):
        self.pool = threadpool.ThreadPool(threadNum)
        self.requests = threadpool.makeRequests(threadReqFunc, threadReqList)
        self.threadCreating = threadCreating
        self.threadDone = threadDone
        self.start_time = time.time()
    
    def start(self):
        for req in self.requests:
            self.threadCreating(req)
            self.pool.putRequest(req)

        self.pool.wait()
        consume_time = '%d second'% (time.time() - self.start_time)
        self.threadDone(consume_time)
    