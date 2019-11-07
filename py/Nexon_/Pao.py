from Nexon_.NexonObject import NexonObject
class Pao(NexonObject):
    def __init__(self,screen,images,baoRow,baoCol):
        self.screen = screen
        self.images = images
        self.image = self.images[0]
        self.col = baoCol
        self.row = baoRow
        self.index = 0
        self.life = 40
        #泡泡延展性
        self.UP = True
        self.DOWN = True
        self.LEFT = True
        self.RIGHT = True
        super(Pao,self).__init__(screen,self.image,self.row,self.col)
    def step(self):
        self.index += 1
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]
        #生命值减少
        self.life -= 1