import chrome_action as action
import tools
import time

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
            tools.download_file(url=url, fileName='./img/' + str(alt))
    
    def multiThreadCreating(req):
        # print(req)
        print()

    def multiThreadDone(time):
        print(time)

    # 获取页面实例
    page = action.getPage('https://www.bilibili.com/')
    # 加载自定义 js 脚本
    action.load_script ('./js_script.js', page)
    # 等待 js 执行 完成
    time.sleep(10)
    # 获取页面源码
    pageSource = action.getPageSource(page)
    # 获取 img tags
    imgTags = tools.get_img_tags(pageSource)
    # 下载 img tags
    multiThread = tools.createMultiThread(
        threadNum=4,
        threadReqFunc=download_img,
        threadReqList=imgTags,
        threadCreating=multiThreadCreating,
        threadDone=multiThreadDone)
    multiThread.start()

bilibili()

# def cosplayjavpl(url):
#     # 获取页面实例
#     page = action.getPage(url)
#     # 等待浏览器检查
#     time.sleep(10)
#     # 加载自定义 js 脚本
#     action.load_script ('./js_script.js', page)
#     # 等待 js 执行 完成
#     time.sleep(10)
#     # 获取页面源码
#     pageSource = action.getPageSource(page)
    

# cosplayjavpl('http://cosplayjav.pl')
