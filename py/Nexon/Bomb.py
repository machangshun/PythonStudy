from Nexon.NexonObject import NexonObject

class Bomb(NexonObject):
    def __init__(self, screen, row, col, image):
        self.screen = screen
        self.row = row
        self.col = col
        self.image = image

        super(Bomb, self).__init__(screen, self.row, self.col, self.image)
        self.index = 0
        self.life = 8

    def bombing(self):
        self.life -= 1

