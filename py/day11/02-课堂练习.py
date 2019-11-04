'''
02-小弹球

'''
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
        self.screen = pygame.display.set_mode((600,600),0,0)
        #1.2初始化坐标
        self.xx = 300
        self.yy = 15
        self.flag = 0
    #2.主函数
    def menu(self):
        #2.1设置窗口标题
        pygame.display.set_caption("满天星")
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

        if self.xx == 15:
            self.flag = 0
        elif self.yy == 585:
            self.flag = 1
        elif self.xx == 585:
            self.flag = 2
        elif self.yy == 15:
            self.flag = 3
        if self.flag == 0:
            self.xx += 1
            self.yy += 1
        elif self.flag == 1:
            self.xx += 1
            self.yy -= 1
        elif self.flag == 2:
            self.xx -= 1
            self.yy -= 1
        elif self.flag == 3:
            self.xx -= 1
            self.yy += 1

    #4.绘制函数
    def paint(self):
        pygame.draw.circle(self.screen,(255,255,255),(self.xx,self.yy),15,0)
if __name__ == '__main__':
    star = MyStar()
    star.menu()
