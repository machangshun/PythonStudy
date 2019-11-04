'''
setting图片处理类
'''
import pygame
class Setting(object):
    def __init__(self):
        #背景图
        self.background = pygame.image.load("background.jpg")
    def getHeroImage(self):
        list = []
        for i in range(0,10):
            list.append(pygame.image.load("ws0%d.png"%i))
        return list