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
imgTags = action.get_pic('https://www.bilibili.com/')
for i in range(len(imgTags)):
    print(imgTags[i])
