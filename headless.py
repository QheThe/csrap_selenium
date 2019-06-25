import time
import threadpool
import chrome_action as action

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
    print (imgTags) 

bilibili()

# imgTags = action.get_pic('https://www.bilibili.com/')
# for i in range(len(imgTags)):
#     print(imgTags[i].get('src'))
#     print(imgTags[i].get('alt'))
