def parseHtml(pageSource):
    from bs4 import BeautifulSoup
    import lxml
    return BeautifulSoup(pageSource, 'lxml')

def get_img_tags(pageSource):
    parsedHtml = parseHtml(pageSource)
    imgTags = parsedHtml.find_all('img')
    return imgTags

def download_file(url):
    import urllib
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

class createMultiThread:
    def __init__(self, threadNum, threadReqFunc, threadReqList, creating, done):
        import threadpool
        import time
        self.pool = threadpool.ThreadPool(threadNum)
        self.requests = threadpool.makeRequests(threadReqFunc, threadReqList)
        self.creating = creating
        self.done = done
        self.start_time = time.time()
    
    def start(self):
        for req in self.requests:
            self.creating(req)
            self.pool.putRequest(req)

        self.pool.wait()
        consume_time = '%d second'% (time.time() - self.start_time)
        self.done(consume_time)
    