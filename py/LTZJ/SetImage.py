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
        # 3. 英雄机子弹
        self.bulletsImage = pygame.image.load("img/bullets.png")
        # 4.敌机图片列表
        self.flysImageList = self.getImage(6,"flys")
        # 5.爱心图片列表
        self.loveImageList = self.getImages(9,"qq")
        # 6.Boss机图片列表
        self.bossImages = [
            [
                pygame.image.load("img/bosss0.PNG"),
                pygame.image.load("img/bosss1.PNG")
            ],
            [
                pygame.image.load("img/boss0.png"),
                pygame.image.load("img/boss1.png")
            ]
        ]
        # 7.Boss机子弹列表
        self.bossBullet = [
            pygame.image.load("img/bossbu.png"),
            pygame.image.load("img/bossbu0.png"),
            pygame.image.load("img/bossbu1.png")

        ]


    # 2.获取英雄机图片列表
    def getHeroImage(self):
        list = []
        for i in range(0,10):
            list.append(pygame.image.load("img/ws0%d.png"%i))
        return list

    # 3.获取图片列表
    def getImage(self,count,name):
        list = []
        for i in range(0,count):
            list.append(pygame.image.load("img/%s%d.png"%(name,i)))
        return list

    # 4.获取图片列表
    def getImages(self,count,name):
        list = []
        for i in range(0,count):
            list.append(pygame.image.load("img/%s%02d.png"%(name,i)))
        return list