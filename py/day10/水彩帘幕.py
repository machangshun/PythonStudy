import pygame
import sys
import random
'''
绘制水彩帘幕
'''
class Curtain(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800,800),0,0)
        self.xx = self.initLocation(100, 800)
        self.yy = self.initLocation(100, 800)
    def initLocation(self,index,coord):
        list = []
        for ix in range(0,index):
            list.append(random.randint(0,coord))
        return list

    def menu(self):
        pygame.display.set_caption("水彩帘幕")

        while True:
            self.screen.fill((0,0,0))
            self.action()
            self.paint()

            pygame.display.update()
    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for ix in range(0,100):
            self.yy[ix] += 1
            if self.yy[ix] > 800:
                self.yy[ix] = 0
    def paint(self):
        pygame.font.init()
        font = pygame.font.Font("simkai.ttf",28)
        for ix in range(0,100):
            num = random.randint(0, 255)
            num1 = random.randint(0, 255)
            num2 = random.randint(0, 255)
            fontRead = font.render("马昌顺", True, (num,num1,num2))
            self.screen.blit(fontRead,(self.xx[ix],self.yy[ix]))

if __name__ == '__main__':
    curtian = Curtain()
    curtian.menu()