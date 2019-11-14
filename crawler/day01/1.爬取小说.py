'''
从零开始
'''
#导入爬取网页模块
from urllib import request
from bs4 import BeautifulSoup
#1.设置URL地址
url = "https://www.biquge18.com/book/100320/0.html"
#设置用户代理
header = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}
#3.设置请求
req = request.Request(url,headers = header)
#打开网页
response = request.urlopen(req)
#读取网页信息
html = response.read()
#6.输出网页
print(html)
'''内容解析'''
#7.解析网页内容
soup = BeautifulSoup(html,"html.parser")
#8.获取信息内容
soup_text = soup.find_all('div',id = "content")
#输出信息
print(soup_text)