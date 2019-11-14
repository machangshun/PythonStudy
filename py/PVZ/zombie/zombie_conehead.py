'''
zombie_conehead
无头僵尸
'''
import pygame,random
from zombie.zombieObject import ZombieObject
from setImage import setImage
sets = setImage()


class Zombie_conehead(ZombieObject):

    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.x = 1000
        self.y = 10 + random.randint(0, 4) * 100
        self.life = 8
        self.damage = 1

        super(Zombie_conehead, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)
        self.index = 0
        self.headFlag = True
    def step(self,sets):
        if self.images == sets.zombie_coneheadImages or self.images == sets.zombieLostHeadImages or self.images == sets.zombie_normalImages:
            self.x -= 1
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        self.image = self.images[int(ix)]
