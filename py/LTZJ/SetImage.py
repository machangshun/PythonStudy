'''
SetImage
'''
'''
图片处理类
'''
import pygame
class Setting(object):
    def __init__(self):
        # 1. 背景图
        self.background = pygame.image.load("background.jpg")
        # 2. 英雄机图片列表
        self.heroImageList = self.getHeroImage()


    # 2.获取英雄机图片列表
    def getHeroImage(self):
        list = []
        for i in range(0,10):
            list.append(pygame.image.load("ws0%d.png"%i))
        return list



