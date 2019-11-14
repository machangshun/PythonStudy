'''
zombie_dead
无头的僵尸
'''
import pygame
from zombie.zombieObject import ZombieObject

class Zombie_dead(ZombieObject):
    def __init__(self, screen, images, x, y):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.x = x
        self.y = y
        self.life = 1
        self.damage = 0
        super(Zombie_dead, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)

        self.index = 0
        self.reloadFlag = 0

    def step(self,sets):
        self.index += 1
        ix = self.index / (len(self.images)/2) % len(self.images)
        self.image = self.images[int(ix)]
        if ix == len(self.images)/2:
            self.reloadFlag = 1
