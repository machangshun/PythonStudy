'''
仙人掌类
'''
from plant.plant import Plant
from setImage import setImage
from bullet import Bullet
from Para import Para

sets = setImage()
para = Para

class Cactus(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Cactus, self).__init__(screen, self.x, self.y, self.image)
        # step要用到的index
        self.index = 0
        self.life = 200
        self.sunshine = 125
        self.interval = 300

    def step(self):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            para.bullets.append(self.shootBy(sets.cactusBulletImg))
            self.index = 0
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]

        # 子弹生成
    def shootBy(self, image):
        bs = Bullet(self.screen, image, self.x + 55, self.y+5, 1)
        return bs

