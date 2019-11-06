from Nexon.NexonObject import NexonObject


class Distory(NexonObject):
    def __init__(self, screen, row, col, images):
        self.screen = screen
        self.row = row
        self.col = col
        self.images = images
        self.image = images[0]
        super(Distory, self).__init__(screen, self.row, self.col, self.image)
        self.index = 0
        self.life = 10

    def animation(self):
        self.index += 1
        self.life -= 1
        ix = self.index / 4 % len(self.images)
        self.image = self.images[int(ix)]

