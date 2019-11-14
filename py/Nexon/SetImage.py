'''
SetImage
图片处理类
'''
import pygame
class SetImage(object):
    def __init__(self):
        self.backImage = pygame.image.load("img/zhan2.jpg")
        self.floorImages = [
            pygame.image.load("img/diban1.png"),
            pygame.image.load("img/diban3.png"),
            pygame.image.load("img/diban4.png")
        ]
        self.buildImages = [
            pygame.image.load("img/shu.png"),
            pygame.image.load("img/red.png"),
            pygame.image.load("img/orange.png"),
            pygame.image.load("img/redHouse.png"),
            pygame.image.load("img/yellowHose.png"),
            pygame.image.load("img/blueHose.png"),
            pygame.image.load("img/box.png")
        ]
        self.baoImages = [
            pygame.image.load("img/up.png"),
            pygame.image.load("img/down.png"),
            pygame.image.load("img/left.png"),
            pygame.image.load("img/right.png")
        ]
        self.haiImages = [
            pygame.image.load("img/ComputerUp.png"),
            pygame.image.load("img/ComputerDown.png"),
            pygame.image.load("img/ComputerLeft.png"),
            pygame.image.load("img/ComputerRight.png")
        ]
        self.paoImages = [
            pygame.image.load("img/PP1.png"),
            pygame.image.load("img/PP2.png")
        ]
        self.bombImages = [
            pygame.image.load("img/bombUP.png"),
            pygame.image.load("img/bombing.png")
        ]
        self.destoryImages = [
            pygame.image.load("img/destroy0.png"),
            pygame.image.load("img/destroy1.png"),
            pygame.image.load("img/destroy2.png"),
            pygame.image.load("img/destroy3.png")
        ]
        self.propImages = [
            pygame.image.load("img/hanbingxie.png"),
            pygame.image.load("img/yaoshui.png"),
            pygame.image.load("img/paoPower.png")

        ]