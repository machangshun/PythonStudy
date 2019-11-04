from LTZJ.flyObject import FlyObject
class Bullet(FlyObject):
    def __init__(self,screen,image,heroX,heroY):
        self.screen = screen
        self.image = image

        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.x = heroX
        self.y = heroY
        super(Bullet,self).__init__(screen,self.image,self.x,self.y)

    #重写走一步
    def step(self):
        #修改坐标值
        self.y -= 1
        #2.动画效果