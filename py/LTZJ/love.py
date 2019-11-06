'''
love
爱心
'''
from LTZJ.flyObject import FlyObject
from LTZJ.Award import Award
import random
class Love(FlyObject,Award):
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.width = self.image.get_rect()[2]
        self.x = random.randint(0,512-self.width)
        self.y = -random.randint(0,768)
        self.flag = 0
        self.index = 0
        self.awardType = random.randint(0,3)
        super(Love,self).__init__(screen,self.image,self.x,self.y)

    def step(self):
        self.index += 1
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]
        if self.x >= 512-self.width:
            self.flag = 1
        elif self.x <= 0:
            self.flag = 0

        if self.flag == 1:
            self.x -= 1
        else:
            self.x += 1
        self.y +=1
    def getAward(self):
        return self.awardType