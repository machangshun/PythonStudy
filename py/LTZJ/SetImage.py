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
        self.flysImageList = self.getflysImage()
        self.loveImageList = self.getLoveImage()
        self.bossImages = [
            [
                pygame.image.load("img/bosss0.png"),
                pygame.image.load("img/bosss1.png"),
            ],
            [
                pygame.image.load("img/boss0.png"),
                pygame.image.load("img/boss1.png"),
            ]
        ]
        self.bossBullet = [
            pygame.image.load("img/bossbu0.png"),
            pygame.image.load("img/bossbu1.png")
        ]
    # 2.获取英雄机图片列表
    def getHeroImage(self):
        list = []
        for i in range(0,10):
            list.append(pygame.image.load("img/ws0%d.png"%i))
        return list
    #3.敌机
    def getflysImage(self):
        list = []
        for i in range(0,6):
            list.append(pygame.image.load("img/flys%d.png"%i))
        return list
    #爱心
    def getLoveImage(self):
        list = []
        for i in range(0,9):
            list.append(pygame.image.load("img/qq%02d.png"%i))
        return list