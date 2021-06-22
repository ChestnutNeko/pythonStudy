# -*- coding = utf-8 -*-    
# from douban.test1 import py1
# print(py1.myAdd(1,2))

# 获取一个get请求
import urllib.request,urllib.parse
# res = urllib.request.urlopen("http://www.baidu.com")
# print(res.read().decode('utf-8'))

# 获取一个post请求
# data = bytes(urllib.parse.urlencode({"name":"liz"}),encoding="utf-8")
# res2 = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(res2.read().decode("utf-8"))

# 超时处理
# try:
#     res3 = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
#     print(res3.read().decode("utf-8"))
# except urllib.error.URLError as error:
#     print("time out!")

# res4 = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
# print(res4.status)
# print(res4.getheaders())
# 418 被发现，我是一个茶壶

# url = "http://httpbin.org/post"
url = "https://www.douban.com"
data = bytes(urllib.parse.urlencode({"name":"liz"}),encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
res = urllib.request.urlopen(req)
print(res.read().decode("utf-8"))