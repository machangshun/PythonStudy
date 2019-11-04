from LTZJ_1.flyObject import FlyObject
class Hero(FlyObject):
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        self.x = 100
        self.y = 100
        '''
        调用父类：super
        '''
        super(Hero,self).__init__(screen,self.images,self.x,self.y)