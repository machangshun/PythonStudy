from LTZJ_2.flyObject import FlyObject
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

    #重写走一步
    def step(self):
        #修改坐标值
        self.y += 2
        #2.动画效果
        self.index += 1
        ix = self.index / 10 % 2
        self.image = self.images[int(ix)]