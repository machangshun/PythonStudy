'''
坚果类
'''
from plant.plant import Plant
from setImage import setImage

sets = setImage()

class Wallnut(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Wallnut,self).__init__(screen, self.x, self.y, self.image)
        # step要用到的index
        self.index = 0
        self.life = 200
        self.sunshine = 50
        self.cd = 10


    def step(self):
        self.index += 1
        # 更改图片
        if self.life == 150:
            self.images = sets.WallNutCracked
        if self.life == 50:
            self.images = sets.WallNutBadlyCracked
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]