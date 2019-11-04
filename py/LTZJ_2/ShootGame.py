'''
雷霆战机
'''
"""
雷霆战机
1.架构整个框架

2.背景绘制
    2.1 新建类 setting类===>存储所有的图片处理
    2.2 导入 第一区域 声明属性 self.set ===>Setting(类)==>background(属性)
    2.3 绘制图片 第四区域  4.1 paintBack() 子函数
    2.4.背景移动 第一区域  1.3 设置背景移动坐标  self.backY
3.英雄机
    3.1  窗口对象,x,y,w,h==>飞行物的特征  父类  FlyObejct==》所有的子类继承
    3.2 新建类 Hero 初始化所有的属性值
    3.3 第一区域 设置英雄机属性  self.hero
    3.4 第四区域 绘制英雄机 

    3.5FlyObject类中 添加抽象函数step函数 子类必须重写
    3.6Hero类中 重写step函数
    3.7第三区域 3.3设置走一步业务处理函数 stepAction()

    3.8 第三区域 3.4 设置英雄机跟随鼠标移动
    3.9Hero类中 添加moveTo(mX,mY)

4.子弹
    4.1新建类Bullet类 继承FlyObject
    4.2第一区域 声明变量self.bullets 存储英雄机子弹
    4.3第三区域 3.5enterAction函数 添加子弹到列表中
    4.4SetImage类中 1.3 设置变量 bulletsImage
    4.5第四区域 4.3 绘制英雄机子弹paintBullet()
    4.6第三区域 3.3stepAction 调用英雄机子弹走一步
    4.7第一区域 声明变量 self.enterIndex = 0 频率值
    4.8第三区域 3.5 enterAction中调整频率值
    4.9第三区域 3.5 enter Action中调整坐标值

5.敌机
    5.1新建AirPlane类 继承FlyObject
        注意事项：坐标轴 随机产生 
    5.2第一区域 声明变量 self.flys = []
    5,3第三区域 3.5 enterAction函数 添加飞行物对象
    5.4 第四区域 4.4调用paintFly()
    5.5第四区域 4.4循环遍历所有的敌机并调用blitMe()函数
    5.6第三区域 3.3stepAction函数 遍历 调用step函数
    5.7第三区域 3.5函数中 调整生成频率值

作业：
1.爱心 Love 走S型
2.boss机 由下往上 再往下 在350 > y 内反弹
3.由上往下4课子弹 BossBullet
"""
import  pygame,sys,random
from LTZJ_2.SetImage import Setting
from LTZJ_2.hero import  Hero
from LTZJ_2.bullet import Bullet
from LTZJ_2.airplane import AirPlane
from LTZJ_2.love import Love
from LTZJ_2.bossplane import BossPlane
from LTZJ_2.bossbullet import BossBullet
class ShootGame(object):
    '''第一区域:变量声明区域'''
    def __init__(self):
        # 1.1 设置窗口
        self.screen = pygame.display.set_mode((512,768),0,0)
        # 1.2 设置属性
        self.setImage = Setting()
        # 1.3 设置Y坐标
        self.backY = 0
        # 1.4 设置英雄机
        self.hero = Hero(self.screen,self.setImage.heroImageList)
        #1.5设置英雄机子弹列表
        self.bullets = []
        #1.6频率值
        self.enterIndex = 0
        #敌机
        self.flys = []
        #love
        self.love = []
        #boss机
        self.flag = 4
        self.boss = BossPlane(self.screen,self.setImage.boss)
        self.bossbu = []
        self.flag = 0
    '''第二区域:main函数区域'''
    def main(self):
        # 2.1 设置窗口标题
        pygame.display.set_caption("雷霆战机")
        # 2.2 设置死循环
        while True:
            # 2.4 设置背景颜色
            self.screen.fill((255,255,255))
            # 2.5 设置业务处理函数
            self.action()
            # 2.6 设置绘制好函数
            self.paint()
            # 2.3 设置刷新屏幕
            pygame.display.update()

    '''第三区域:业务处理函数区域'''
    def action(self):
        # 3.1 循环遍历所有的监听事件
        for event in pygame.event.get():
            # 3.2 判断是否退出
            if event.type == pygame.QUIT:
                sys.exit()
        '''
        业务处理区域
        '''
        #3.3走一步业务
        self.stepAction()
        #3.4跟随鼠标移动
        mouseX,mouseY = pygame.mouse.get_pos()
        self.hero.moveTo(mouseX,mouseY)
        #3.5设置调用生成函数
        self.enterAction()
    #3.3走一步函数
    def stepAction(self):
        #1.调用英雄机走一步函数
        self.hero.step()
        print(self.hero)
        for bt in self.bullets:
            bt.step()
        for fly in self.flys:
            fly.step()
        for love_ in self.love:
            love_.step()
        self.boss.step()
        for bu in self.bossbu:
            bu.step()

    #3.5调用生成函数
    def enterAction(self):
        #修改频率值
        self.enterIndex += 1
        #1.生成英雄机子弹
        if self.enterIndex%20 == 0:
            #调整坐标
            btX = self.hero.x + self.hero.width/2
            btY = self.hero.y - 10
            bt = Bullet(self.screen, self.setImage.bulletsImage, btX,btY)
            self.bullets.append(bt)
        if self.enterIndex%100 == 0:
            bossX = self.boss.x + self.boss.width/2 - 50
            bossY = self.boss.y + 200
            if self.boss.flag != 4:
                self.bossbu.append(BossBullet(self.screen, self.setImage.bossbu, bossX, bossY))
                self.bossbu.append(BossBullet(self.screen, self.setImage.bossbu, bossX-50, bossY))
                self.bossbu.append(BossBullet(self.screen, self.setImage.bossbu, bossX + 100, bossY))
                self.bossbu.append(BossBullet(self.screen, self.setImage.bossbu, bossX + 150, bossY))

        if self.enterIndex%100 == 0:
            ap = AirPlane(self.screen,self.setImage.flysImageList)
            self.flys.append(ap)
        if self.enterIndex%500 == 0:
            self.love.append(Love(self.screen, self.setImage.loveImageList))
        # if self.enterIndex%1000 == 0:
        #     if self.flag == 0:
        #         self.boss.append(BossPlane(self.screen, self.setImage.boss))
        #         self.flag = 1
        #     else:
        #         pass


    '''第四区域:绘制函数区域'''
    def paint(self):
        # 4.1 绘制背景
        self.paintBack()
        # 4.2 绘制英雄机
        self.hero.blitMe()
        #4.3绘制英雄机子弹
        self.paintBullet()
        self.paintBossbu()
        #4.4绘制敌机
        self.paintFly()
        #4.5绘制爱心
        self.paintLove()
        #4.6绘制boss
        #self.paintBoss()
        self.boss.blitMe()
    # 4.1 绘制背景图
    def paintBack(self):
        # 修改背景图坐标
        self.backY += 1
        # 绘制背景
        self.screen.blit(self.setImage.background,(0,self.backY))
        # 绘制背景图
        self.screen.blit(self.setImage.background,(0,-768+self.backY))
        # 循环
        if self.backY > 768:
            self.backY = 0

    #4.3绘制英雄机子弹
    def paintBullet(self):
        for bt in self.bullets:
            bt.blitMe()
    def paintBossbu(self):
        for bu in self.bossbu:
            bu.blitMe()
    #4.4绘制敌机
    def paintFly(self):
        for fly in self.flys:
            fly.blitMe()

    #4.5绘制爱心
    def paintLove(self):
        for love_ in self.love:
            love_.blitMe()
    #绘制boss
    # def paintBoss(self):
    #     for boss_ in self.boss:
    #         boss_.blitMe()


if __name__ == '__main__':
    game = ShootGame()
    game.main()

