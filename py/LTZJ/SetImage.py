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
        self.background = pygame.image.load("img/background.jpg")
        # 2. 英雄机图片列表
        self.heroImageList = self.getHeroImage()
        #3.英雄机子弹
        self.bulletsImage = pygame.image.load("img/bullets.png")

    # 2.获取英雄机图片列表
    def getHeroImage(self):
        list = []
        for i in range(0,10):
            list.append(pygame.image.load("img/ws0%d.png"%i))
        return list




