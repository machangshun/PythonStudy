'''
tankObject
坦克
'''
import pygame,abc
class TankObject(object):
    def __init__(self,screen,images,x,y):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.x = x
        self.y = y
    @abc.abstractmethod
    def blitMe(self):
        self.screen.blit(self.image,(self.x,self.y))