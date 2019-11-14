'''
Bao
宝宝
'''
from NexonObject import NexonObject
class Bao(NexonObject):
    def __init__(self,screen,images):
        self.screen = screen
        self.images = images
        #上下左右 0，1，2，3
        self.image = self.images[1]
        #设置行列
        self.row = 0
        self.col = 6
        self.speed = 1
        self.number = 1
        self.power = 1
        #调用父类初始化函数
        super(Bao,self).__init__(screen,self.image,self.row,self.col)

    #2.移动函数
    def step(self,dir):
        if dir == 0:
            self.row -= 1
        if dir == 1:
            self.row += 1
        if dir == 2:
            self.col -= 1
        if dir == 3:
            self.col += 1
        self.image = self.images[dir]
