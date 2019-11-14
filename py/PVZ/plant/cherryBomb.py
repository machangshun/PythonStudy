'''
樱桃炸弹类
'''
from setImage import setImage
from plant.plant import Plant
from Para import Para
from zombie.zombie_dead import Zombie_dead
import pygame

# 图片路径的全局变量
sets = setImage()
para = Para

class CherryBomb(Plant):
    def __init__(self, screen, x, y, images, state):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        super(CherryBomb, self).__init__(screen, self.x, self.y, self.image)
        self.index = 0
        self.life = 50
        # 所需的阳光数
        self.sunshine = 150
        # 产生阳光的间隔 单位次数
        self.interval = 50
        # 是否变到最大的标志
        self.isBigest = 0
        self.para = Para

    # 樱桃炸弹的功能，爆炸，并且杀死僵尸兵，执行之后消失
    def function(self):
        # 樱桃炸弹变大
        for i in range(len(self.para.paintPlants)):
            # 判断是否是樱桃炸弹，是的话就去掉该对象
            if isinstance(self.para.paintPlants[i], CherryBomb):
                # 此处是遍历僵尸列表，消灭在爆炸范围之内的全部僵尸
                self.para.gridList[self.gridX][self.gridY] = -1
                del self.para.paintPlants[i]
                break

    # 樱桃炸弹爆炸一次之后就死亡
    def step(self):
        self.index += 1
        # 樱桃炸弹逐渐变大 , 在更改images后变为爆炸效果
        ix = self.index / 5 % len(self.images)
        self.image = self.images[int(ix)]
        # 变到最大之后，调用樱桃炸弹的爆炸功能，并且更改images
        if self.isBigest == 0 and self.index == 70:
            self.images = sets.CherryBombBoom
            self.image = self.images[0]
            self.width = self.image.get_rect()[2]
            self.height = self.image.get_rect()[3]
            # 重新调整绘图位置
            self.x -= 60
            self.y -= 60
            self.index = 0
            self.isBigest = 1

        # 当炸弹范围变到最大时，对僵尸造成伤害
        if ix == 7 and self.isBigest == 1:
            # 遍历僵尸列表
            for zombie in para.zombies:
                # 对 3X3 范围内的僵尸统一造成5点伤害
                # 用僵尸脚的两个点判断是否被樱桃炸弹炸到
                if zombie.y + 100 > self.y - 80 and zombie.y + 100 <self.y + self.height and \
                        ((zombie.x > self.x and zombie.x < self.x + self.width)
                     or (zombie.x + zombie.width > self.x and
                         zombie.x + zombie.width < self.x + self.width)):
                    zombie.life -= 1000
                    if zombie.life <= 0:
                        para.zombies.append(Zombie_dead(self.screen, sets.zombie_charred, zombie.x+50, zombie.y+20))
                        para.zombies.remove(zombie)

        if self.isBigest == 1 and self.index == 130:
            self.function()