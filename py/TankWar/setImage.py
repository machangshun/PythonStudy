'''
加载图片
'''
import pygame
class SetImage(object):
    def __init__(self):
        self.backImage = pygame.image.load("img/background.png")
        self.MyTank_1 = [
            pygame.image.load("img/tank_T1_0.png").subsurface((0,0),(48,48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((48, 0), (48, 48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((0, 48), (48, 48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((48, 48), (48, 48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((0, 96), (48, 48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((48, 96), (48, 48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((0, 144), (48, 48)),
            pygame.image.load("img/tank_T1_0.png").subsurface((48, 144), (48, 48)),
            pygame.image.load("img/tank_T1_1.png"),
            pygame.image.load("img/tank_T1_2.png")
        ]
        self.MyTank_2 = [
            pygame.image.load("img/tank_T2_0.png"),
            pygame.image.load("img/tank_T2_1.png"),
            pygame.image.load("img/tank_T2_2.png")
        ]
        self.buildImages = [
            pygame.image.load("img/brick.png"),
            pygame.image.load("img/iron.png")
        ]
        self.homeImages = [
            pygame.image.load("img/home.png"),
            pygame.image.load("img/home1.png"),
            pygame.image.load("img/home_destroyed.png")
        ]
