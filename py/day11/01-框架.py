import pygame
import sys
import random
'''
1.100颗小星星在屏幕上（不能移动）
2.颜色不同
3.由左上角往右下角移动
'''
class MyStar(object):
    #1.初始化函数
    def __init__(self):
        #1.1窗口设置(长，宽)
        self.screen = pygame.display.set_mode((800,600),0,0)
        #1.2初始化坐标
        self.xx = self.initLocation(100,800)
        self.yy = self.initLocation(100,600)
    #初始化坐标
    def initLocation(self,index,coord):
        #空列表
        list = []
        #循环遍历
        for ix in range(0,index):
            list.append(random.randint(0,coord))
        #将得到随机列表
        return list
    #2.主函数
    def menu(self):
        #2.1设置窗口标题
        pygame.display.set_caption("小弹球")
        #2.2设置死循环
        while True:
            #2.5.设置背景颜色()元组RGB(,,)0为最暗，255为最亮
            self.screen.fill((0,0,0))
            #2.4业务处理函数
            self.action()
            #2.6绘制函数
            self.paint()
            #2.3设置刷新窗口
            pygame.display.update()
    #3.业务处理函数
    def action(self):
        #3.1遍历所有的监听事件
        for event in pygame.event.get():
            #3.2判断是否点击了退出
            if event.type == pygame.QUIT:
                sys.exit()
    #4.绘制函数
    def paint(self):
        #4.1字体初始化
        pygame.font.init()
        #4.2字体设置
        font = pygame.font.Font("simkai.ttf",28)
        #4.3字体内容设置(绘制内容，可见，（颜色值）)
        fontRead = font.render("*",True,(0,255,255))
        #4.4字体设置坐标
        self.screen.blit(fontRead,(50,50))
if __name__ == '__main__':
    star = MyStar()
    star.menu()
