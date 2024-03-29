"""
僵尸父类
1.图片image
2.x,y,width,height
3.damage life 伤害 生命
4.限定活动区域 重写该方法
5.step 走一步 重写该方法
6.blitme 绘图方法
7.hit 碰撞方法
"""
import abc


class ZombieObject(object):
    def __init__(self, screen, x, y, image, life, damage):
        # 获取屏幕
        self.screen = screen
        # 获取坐标
        self.x = x
        self.y = y
        # 获取图片
        self.image = image
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.life = life
        self.damage = damage
        self.headFlag = True

    def outOfBounds(self):
        return self.x < 100

    @abc.abstractmethod
    def step(self,sets):
        self.x -= 1

    # 绘图方法
    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 子弹与僵尸碰撞
    def hitBy(self, bt):
        # 1.获取子弹的坐标值
        btX = bt.x
        btY = bt.y
        btYH = bt.y + bt.height
        # 2.获取僵尸的坐标值
        zX = self.x + self.width/2
        zY = self.y
        zYH = self.y + self.height
        # 3.返回判断值
        return zX >= btX-5and zX <= btX + 5 and zY < btY and zYH > btYH
