"""
铁桶僵尸
"""
import pygame, random
from zombie.zombieObject import ZombieObject
from setImage import setImage
sets = setImage()

class Zombie_bucket(ZombieObject):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        # 取值范围暂定
        self.x = 1000
        self.y = 30 + random.randint(0, 4)*100
        self.life = 20
        self.damage = 1
        super(Zombie_bucket, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)
        # 图片集转换集
        self.index = 0

    def step(self,sets):
        # 1.更改坐标值
        if self.images == sets.zombie_bucketImages or self.images == sets.zombieLostHeadImages or self.images == sets.zombie_normalImages:
            self.x -= 0.5
        # 2.更改图片
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        # 设置图片
        self.image = self.images[int(ix)]
