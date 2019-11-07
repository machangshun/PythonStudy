from Nexon_.NexonObject import NexonObject
class Bomb(NexonObject):
    def __init__(self,screen,image,paoRow,paoCol):
        self.screen = screen
        self.image = image
        self.row = paoRow
        self.col = paoCol
        self.life = 20
        self.index = 0
        super(Bomb,self).__init__(screen,self.image,self.row,self.col)

    def step(self):
        self.life -= 1


