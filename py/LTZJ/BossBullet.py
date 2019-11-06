from LTZJ.flyObject import FlyObject
class BossBullet(FlyObject):
    def __init__(self,screen,images,bossX,bossY):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.x = bossX
        self.y = bossY
        self.index = 0
        super(BossBullet,self).__init__(screen,self.image,self.x,self.y)

    def step(self):
        self.y += 2
        self.index += 1
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]