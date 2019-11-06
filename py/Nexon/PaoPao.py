from Nexon.NexonObject import NexonObject
from Nexon.Bomb import Bomb

class PaoPao(NexonObject):
    def __init__(self, screen, row, col, images):
        self.screen = screen
        self.row = row
        self.col = col
        self.images = images
        self.image = images[0]
        super(PaoPao, self).__init__(screen, self.row, self.col, self.image)
        self.index = 1
        self.life = 88

    def animation(self):
       self.index += 1
       self.life -= 1
       ix = self.index / 10 % len(self.images)
       self.image = self.images[int(ix)]