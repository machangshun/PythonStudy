class FlyObject(object):
    def __init__(self,screen,image,x,y):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        #get_rect == > x,y,w,h =>获取图片宽度和高度
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]

    def blitMe(self):
        self.screen.blit(self.image,(self.x,self.y))