'''
jj
'''
from LTZJ.flyObject import FlyObject
'''
'''
class Jj(FlyObject):
    # 1.初始化函数 screen,image,x,y
    def __init__(self,screen,images):
        # 1.1 设置窗口
        self.screen = screen
        # 1.2 设置图片列表
        self.images = images
        # 1.3 设置图片
        self.image = self.images[0]
        # 1.4 设置坐标
        self.x = 100
        self.y = 100
        self.index = 0
        '''调用父类
        super:调用父类
        '''
        super(Jj,self).__init__(screen,self.image,self.x,self.y)

    #2.走一步函数
    def step(self):
        pass
    #3.鼠标移动
    def moveTo(self,mouseX,mouseY):
        self.x = mouseX-self.width/2
        self.y = mouseY-self.height/2