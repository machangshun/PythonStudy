'''
flyObject
'''
'''
所有类的父类
'''
import  abc
class FlyObject(object):
    # 1.初始化函数
    def __init__(self,screen,image,x,y):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        # get_rect===>x,y,w,h===>获取宽度和高度
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]


    # 2.绘制自己
    '''
    所有的子类都拥有该函数
    '''
    def blitMe(self):
        self.screen.blit(self.image,(self.x,self.y))

    @abc.abstractclassmethod
    def step(self):
       pass
    #4.碰撞函数 共有函数 所有子类都有
    def hitBy(self,bt):
        #子弹边界
        btX = bt.x
        btY = bt.y
        btXW = bt.x + bt.width
        btYH = bt.y + bt.height
        #飞行物边界
        flyX = self.x
        flyY = self.y
        flyXW = self.x + self.width
        flyYH = self.y + self.height

        return btX > flyX and btXW < flyXW and btY > flyY and btYH < flyYH
