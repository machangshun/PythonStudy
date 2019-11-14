from NexonObject import NexonObject
import random
class Prop(NexonObject):
    def __init__(self,screen,images,dRow,dCol):
        self.screen = screen
        self.images = images
        self.num = random.randint(0,2)
        self.image = self.images[self.num]
        self.row = dRow
        self.col = dCol
        super(Prop,self).__init__(screen,self.image,self.row,self.col)