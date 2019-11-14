'''
MyTank
'''
from TankWar.TankObject import TankObject
class myTank(TankObject):
    def __int__(self,screen,images):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.x = 8*24 + 3
        self.y = 24*24 + 3
        super(myTank,self).__init__(screen,self.image,self.x,self.y)
    def step(self,dir):
        if dir == 0:
            self.y -= 5
            self.image = self.images[dir * 2 + self.y % 2]

        if dir == 1:
            self.y += 5
            self.image = self.images[dir * 2 + self.y % 2]
        if dir == 2:
            self.x -= 5
            self.image = self.images[dir * 2 + self.x % 2]
        if dir == 3:
            self.x += 5
            self.image = self.images[dir * 2 + self.x % 2]
