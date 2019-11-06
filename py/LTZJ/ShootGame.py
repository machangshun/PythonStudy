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
英雄机子弹与boss机碰撞
boss子弹碰撞英雄机
"""
import  pygame,sys,random
from LTZJ.SetImage import Setting
from LTZJ.hero import  Hero
from LTZJ.bullet import Bullet
from LTZJ.airplane import AirPlane
from LTZJ.love import Love
from LTZJ.bossplane import Boss
from LTZJ.BossBullet import BossBullet
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
        self.bss = []
        self.bssBts = []
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
        #调用碰撞函数
        self.hitAction()


    #3.3走一步函数
    def stepAction(self):
        #1.调用英雄机走一步函数
        self.hero.step()
        for bt in self.bullets:
            bt.step()
        for fly in self.flys:
            fly.step()
        for love_ in self.love:
            love_.step()
        for boss in self.bss:
            boss.step()
        for bts in self.bssBts:
            bts.step()
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
            ap = AirPlane(self.screen,self.setImage.flysImageList)
            self.flys.append(ap)
        if self.enterIndex%1000 == 0:
            self.love.append(Love(self.screen, self.setImage.loveImageList))
        if self.enterIndex%500 == 0:
            self.bss.append(Boss(self.screen,self.setImage.bossImages))
        if len(self.bss) > 0 and self.enterIndex % 120 == 0:
            for boss in self.bss:
                if boss.bsIndex == 1:
                    xw = boss.width / 5
                    for i in range(0, 4):
                        self.bssBts.append(
                            BossBullet(self.screen, self.setImage.bossBullet, boss.x + i * xw, boss.y + boss.height))


    def hitAction(self):
        for bt in self.bullets:
            self.hit(bt)
        # for bt in self.bssBts:
        #     self.hit(bt)
    def hit(self,bt):
        #1.设置变量
        hitIndex = -1
        for i in range(0,len(self.flys)):
            #3.进行判断比较
            if self.flys[i].hitBy(bt):
                #4.将下标赋值给hitIndex
                hitIndex = i
                break
        #5.根据碰撞变量判断
        if hitIndex != -1:
            #获取飞行物对象
            fly = self.flys[hitIndex]
            #匹配判断
            if isinstance(fly,Love):
                pass
            if isinstance(fly,AirPlane):
                pass
            #6.删除飞行物
            del self.flys[hitIndex]
            self.bullets.remove(bt)
    '''第四区域:绘制函数区域'''
    def paint(self):
        # 4.1 绘制背景
        self.paintBack()
        # 4.2 绘制英雄机
        self.hero.blitMe()
        #4.3绘制英雄机子弹
        self.paintBullet()
        #4.4绘制敌机
        self.paintFly()
        #4.5绘制爱心
        self.paintLove()
        #4.5绘制boss
        self.paintboss()
        self.paintBossBu()
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

    #4.4绘制敌机
    def paintFly(self):
        for fly in self.flys:
            fly.blitMe()

    #4.5绘制爱心
    def paintLove(self):
        for love_ in self.love:
            love_.blitMe()

    def paintboss(self):
        for boss in self.bss:
            boss.blitMe()
    def paintBossBu(self):
        for bts in self.bssBts:
            bts.blitMe()
if __name__ == '__main__':
    game = ShootGame()
    game.main()

