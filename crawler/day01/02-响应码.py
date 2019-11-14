'''
响应码
'''
from urllib import request
#1.设置URL路径地址
url = "https://www.baidu.com/"
#2.打开URL链接
response = request.urlopen(url)
#读取解码
html = response.read().decode("gbk")
print(html)
#6.查看响应码
print(response.getcode())
#查看服务器响应的HTTP报头
print(response.info())
print(response.geturl())
