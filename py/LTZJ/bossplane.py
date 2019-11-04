'''
bossplane
'''
from LTZJ.flyObject import FlyObject
import random
class BossPlane(FlyObject):
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.x = random.randint(0,512-self.width)
        self.y = random.randint(768,768*2)
        self.index = 0
        self.flag = 4
        super(BossPlane,self).__init__(screen,self.image,self.x,self.y)

        def step(self):
            if self.flag == 4:
                self.y -= 1
            if self.y < 0:
                if self.flag == 4:
                    self.flag = 0
                elif self.flag == 3:
                    self.flag = 0
                else:
                    self.flag = 1
            if self.x > 512 - self.width:
                if self.flag == 0:
                    self.flag = 1
                else:
                    self.flag = 2
            if self.y >= 350 - self.height:
                if self.flag == 1:
                    self.flag = 2
                else:
                    self.flag = 3
            if self.x <= 0:
                if self.flag == 2:
                    self.flag = 3
                else:
                    self.flag = 1

            if self.flag == 0:
                self.x += 1
                self.y += 1
            if self.flag == 1:
                self.x -= 1
                self.y += 1
            if self.flag == 2:
                self.x -= 1
                self.y -= 1
            if self.flag == 3:
                self.x += 1
                self.y -= 1
        self.index += 1
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]
