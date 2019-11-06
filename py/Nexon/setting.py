'''
图片变量设置
        0 代表树
        1 代表红色模块
        2 代表橙色模块
        3 代表红房子
        4 代表黄房子
        5 代表蓝房子
        6 代表箱子
        7 空白
'''
import pygame

class Setting(object):
    def __init__(self):
        self.back = pygame.image.load("img/zhan2.jpg")
        # 地板图
        self.diban0 = pygame.image.load("img/diban1.png")
        self.diban1 = pygame.image.load("img/diban3.png")
        self.diban2 = pygame.image.load("img/diban4.png")

        # 建筑物
        self.house0 = pygame.image.load("img/shu.png")
        self.house1 = pygame.image.load("img/red.png")
        self.house2 = pygame.image.load("img/orange.png")
        self.house3 = pygame.image.load("img/redHouse.png")
        self.house4 = pygame.image.load("img/yellowHose.png")
        self.house5 = pygame.image.load("img/blueHose.png")
        self.house6 = pygame.image.load("img/box.png")


        # 1.5 宝宝图片集
        self.baoImages = [
            pygame.image.load("img/up.png"),
            pygame.image.load("img/down.png"),
            pygame.image.load("img/left.png"),
            pygame.image.load("img/right.png")
        ]

        self.paoImages = [
            pygame.image.load("img/PP1.png"),
            pygame.image.load("img/PP2.png")
        ]

        self.bomb1 = pygame.image.load("img/bombUp.png")
        self.bomb2 = pygame.image.load("img/Bombing.png")

        self.distoryImages = [
            pygame.image.load("img/destroy0.png"),
            pygame.image.load("img/destroy1.png"),
            pygame.image.load("img/destroy2.png"),
            pygame.image.load("img/destroy3.png")
        ]
