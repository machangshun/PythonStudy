from Nexon.NexonObject import NexonObject

class BaoBao(NexonObject):
    def __init__(self, screen, images):
        self.screen = screen
        self.row = 0
        self.col = 13
        self.images = images

        self.image = self.images[1]
        super(BaoBao, self).__init__(screen, self.row, self.col, self.image)

    # 移动函数
