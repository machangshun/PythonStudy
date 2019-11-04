'''
02-小弹球
五个小球向不同方向运动
每撞墙一次改变一次颜色
'''
import pygame
import sys
import random

class MyStar(object):
    #1.初始化函数
    def __init__(self):
        #1.1窗口设置(长，宽)
        self.screen = pygame.display.set_mode((800,600),0,0)
        #1.2初始化坐标
        self.xx = self.initLocation(0,785)
        self.yy = self.initLocation(0,585)
        self.flag = [0,1,2,3,1]
        self.color1 = self.initLocation(0,255)
        self.color2 = self.initLocation(0,255)
        self.color3 = self.initLocation(0,255)
    def initLocation(self,a,b):
        list = []
        for ix in range(0,5):
            list.append(random.randint(a,b))
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
            pygame.time.delay(10)
            #2.3设置刷新窗口
            pygame.display.update()
    #3.业务处理函数
    def action(self):
        #3.1遍历所有的监听事件
        for event in pygame.event.get():
            #3.2判断是否点击了退出
            if event.type == pygame.QUIT:
                sys.exit()
        for ix in range(0,5):
            if self.xx[ix] == 15:
                self.color1[ix] = random.randint(0, 255)
                self.color2[ix] = random.randint(0, 255)
                self.color3[ix] = random.randint(0, 255)
                if self.flag[ix] == 3:
                    self.flag[ix] = 0
                else:
                    self.flag[ix] = 1
            elif self.yy[ix] == 585:
                self.color1[ix] = random.randint(0, 255)
                self.color2[ix] = random.randint(0, 255)
                self.color3[ix] = random.randint(0, 255)
                if self.flag[ix] == 0:
                    self.flag[ix] = 1
                else:
                    self.flag[ix] = 2
            elif self.xx[ix] == 785:
                self.color1[ix] = random.randint(0, 255)
                self.color2[ix] = random.randint(0, 255)
                self.color3[ix] = random.randint(0, 255)
                if self.flag[ix] == 1:
                    self.flag[ix] = 2
                else:
                    self.flag[ix] = 3
            elif self.yy[ix] == 15:
                self.color1[ix] = random.randint(0, 255)
                self.color2[ix] = random.randint(0, 255)
                self.color3[ix] = random.randint(0, 255)
                if self.flag[ix] == 2:
                    self.flag[ix] = 3
                else:
                    self.flag[ix] = 0

            if self.flag[ix] == 0:
                self.xx[ix] += 1
                self.yy[ix] += 1
            elif self.flag[ix] == 1:
                self.xx[ix] += 1
                self.yy[ix] -= 1
            elif self.flag[ix] == 2:
                self.xx[ix] -= 1
                self.yy[ix] -= 1
            elif self.flag[ix] == 3:
                self.xx[ix] -= 1
                self.yy[ix] += 1


    #4.绘制函数
    def paint(self):
        for ix in range(0,5):
            pygame.draw.circle(self.screen, (self.color1[ix],self.color2[ix],self.color3[ix]), (self.xx[ix], self.yy[ix]), 15, 0)

if __name__ == '__main__':
    star = MyStar()
    star.menu()
