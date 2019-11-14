from plant.plant import Plant
from setImage import setImage
from bullet import Bullet
from Para import Para
import threading

sets = setImage()
para = Para
class Repeater(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Repeater,self).__init__(screen, self.x, self.y, self.image)
        # step要用到的index
        self.index = 0
        self.life = 100
        self.sunshine = 200
        self.interval = 150

    def step(self):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            para.bullets.append(self.shootBy(sets.peaBulletImg))
            timer = threading.Timer(0.3, self.shoot)
            timer.start()
            self.index = 0
        # 更改图片
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]


    def shootBy(self, image):
        bs = Bullet(self.screen, image, self.x + 65, self.y + 2, 0)
        return bs

    def shoot(self):
        para.bullets.append(self.shootBy(sets.peaBulletImg))
        print("timer start")