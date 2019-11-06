class NexonObject(object):
    # 初始化函数
    def __init__(self, screen, row, col, image):
        self.screen = screen
        self.row = row
        self.col = col
        self.image = image

    # 2. 绘制自己
    def blitMe(self):
        x = 25 + 50*self.col
        y = 25 + 50*self.row
        self.screen.blit(self.image, (x, y))