'''
敌机类
'''
from LTZJ.flyObject import FlyObject
import random
from LTZJ.Enemy import Enemy
class AirPlane(FlyObject,Enemy):
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

    def getScore(self):
        return 5

    def outofBounds(self):
        if self.y > 768:
            return True
        else:
            return False