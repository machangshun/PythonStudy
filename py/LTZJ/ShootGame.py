'''
雷霆战机
'''
import  pygame,sys
from LTZJ.SetImage import Setting
from LTZJ.hero import  Hero
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
"""
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
    #3.3走一步函数
    def stepAction(self):
        #1.调用英雄机走一步函数
        self.hero.step()


    '''第四区域:绘制函数区域'''
    def paint(self):
        # 4.1 绘制背景
        self.paintBack()
        # 4.2 绘制英雄机
        self.hero.blitMe()


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



if __name__ == '__main__':
    game = ShootGame()
    game.main()

