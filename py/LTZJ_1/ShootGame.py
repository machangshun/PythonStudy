'''
雷霆战机
1.架构整个框架
2.背景绘制
    2.1新建类 setting类==》存储所有的图片处理
    2.2导入第一区域 声明属性 self.set==>setting(类) ==》background
    2.3绘制图片 第四区域 4.1paintBack()
    2.4背景移动 第一区域 1.3 设置背景移动坐标 self.backY
3.英雄机
    3.1窗口对象，x,y,w,h ==>飞行物的特征 父类 FlyObject==>所有子类继承
    3.2新建类Hero 初始化所有的属性值
    3.3第一区域 设置英雄机属性 self.Hero
    3.4第四区域 绘制英雄机


课后作业：
1.看看刚刚所写的雷霆战机
2.找不同
    列表【
        x,y,w,h
        [100,100,30,30],
    】
'''
import pygame,sys
from LTZJ_1.setimage import Setting
from LTZJ_1.hero import Hero
class ShootGame(object):
    def __init__(self):
        #1.1设置窗口
        self.screen =  pygame.display.set_mode((512,768),0,0)
        self.setImage = Setting()
        self.backY = 0
        self.index = 0
        self.hero = Hero(self.screen,self.setImage.getHeroImage()[0])
    '''第二区域：main函数区域'''

    def main(self):
        #2.1设置窗口标题
        pygame.display.set_caption("雷霆战机")
        while True:
            #设置背景颜色
            self.screen.fill((255,255,255))
            self.action()
            self.paint()
            pygame.time.delay(20)
            pygame.display.update()
    '''第三区域：业务处理函数区域'''
    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        self.index += 1
        self.hero = Hero(self.screen,self.setImage.getHeroImage()[self.index])
        if self.index == 9:
            self.index = 0
    '''第四区域：绘制函数区域'''
    def paint(self):
        #4.1绘制背景
        self.paintBack()
        self.hero.blitMe()
    #4.1绘制背景图
    def paintBack(self):
        #修改背景图坐标
        self.backY += 1
        #绘制背景
        self.screen.blit(self.setImage.background,(0,self.backY))
        #绘制背景图
        self.screen.blit(self.setImage.background, (0,-768 + self.backY))
        if self.backY > 768:
            self.backY = 0

if __name__ == '__main__':
    game = ShootGame()
    game.main()