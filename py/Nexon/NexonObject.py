'''
NexonObject
泡泡堂父类
'''
class NexonObject(object):
    def __init__(self,screen,image,row,col):
        self.screen = screen
        self.image = image
        self.row = row
        self.col = col
    #绘制
    def blitMe(self):
        #获取坐标值
        x = self.col * 50 + 25
        y = self.row * 50 + 25
        #绘制图片
        self.screen.blit(self.image,(x,y))
