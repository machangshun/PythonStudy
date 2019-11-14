from NexonObject import NexonObject
class Destory(NexonObject):
    def __init__(self, screen, images, row, col):
        self.screen = screen
        self.row = row
        self.col = col
        self.images = images
        self.image = images[0]
        self.index = 0
        self.life = 20
        super(Destory, self).__init__(screen,self.image,self.row,self.col )

    def step(self):
        self.index += 1
        self.life -= 1
        ix = self.index / 4 % len(self.images)
        self.image = self.images[int(ix)]
