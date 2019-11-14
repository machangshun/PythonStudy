from urllib import request
from bs4 import BeautifulSoup
import os
class Hua(object):
    def __init__(self,url,headers):
        self.contentUrl = url
        self.header = headers
    def main(self):
        #2.1设置URL路径地址开始位置
        index = 30242268
        while index <= 30242476:
            url = "%s%d.html"%(self.contentUrl,index)
            #调用请求函数
            self.requestAction(url)
            #修改参数
            index += 1
    def requestAction(self,url):
        req = request.Request(url,headers = self.header)
        response = request.urlopen(req)
        html = response.read()
        self.clearData(html)
    def clearData(self,html):
        #数据解析
        soup = BeautifulSoup(html, "html.parser")
        soup_title = str(soup.find('title'))
        soup_text = str(soup.find('div', id="content"))
        context = soup_text[soup_text.find("<br/>"):]
        context = context.replace("<br/>", "")
        context = context.replace("<br>", "")
        context = context.replace("</br>", "")
        context = context.replace("</div>", "")
        soup_title = soup_title[7:-18]
        self.saveData(context,soup_title)
    def saveData(self,context,soup_title):
        file = open("%s" % soup_title, "w", encoding="utf-8")
        file.write(context)
        file.close()
if __name__ == '__main__':
    url = "https://www.23wx.so/55_55628/"
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    hua = Hua(url,header)
    os.mkdir('hqg')
    os.chdir('hqg')
    hua.main()