'''
normal zombie
正常的僵尸

'''
import pygame
from zombie.zombieObject import ZombieObject
import random
from setImage import setImage
sets = setImage()

class Zombie_normal(ZombieObject):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.x = 1000
        self.y = 15 + random.randint(0, 4) * 100
        self.life = 5
        self.damage = 1
        super(Zombie_normal, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)
        self.index = 0
        self.headFlag = True
    #走一步：三种状态动画
    def step(self,sets):
        if self.images == sets.zombie_normalImages or self.images == sets.zombieLostHeadImages:
            self.x -= 1
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        self.image = self.images[int(ix)]
