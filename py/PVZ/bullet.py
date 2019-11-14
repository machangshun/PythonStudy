import pygame

class Bullet(object):
    def __init__(self, screen, image, peaX, peaY, type):
        self.screen = screen
        self.image = image
        # x,y
        self.x = peaX
        self.y = peaY
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        # 子弹种类， 0代表豌豆 1代表仙人掌刺
        self.type = type

    def outOfBounds(self):
        return self.x > 996

    def step(self):
        self.x += 5


    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))
