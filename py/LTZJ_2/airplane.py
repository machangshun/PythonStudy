'''
敌机类
'''
from LTZJ_2.flyObject import FlyObject
import random
class AirPlane(FlyObject):
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.x = random.randint(0, 512-65)
        self.y = -random.randint(0, 768)
        self.index = 0
        super(AirPlane, self).__init__(screen, self.image, self.x, self.y)

    def step(self):
        self.y += 1.5
        self.index += 1
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]

