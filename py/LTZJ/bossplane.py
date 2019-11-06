'''
Boss
'''
from LTZJ.flyObject import FlyObject
import  random
class Boss(FlyObject):
    # 1.初始化函数
    def __init__(self,screen,images):
        self.screen = screen
        '''
        二维图片列表
        [
        第一套动作
        第二套动作
        ]
        
        '''
        self.images = images
        #  变换动画效果参数
        self.bsIndex = 0
        self.image = self.images[self.bsIndex][0]
        self.width = self.image.get_rect()[2]
        self.height= self.image.get_rect()[3]
        self.x = 512/2 - self.width/2
        self.y = 768+random.randint(0,768)
        # 动画效果
        self.life = 100
        self.index = 0
        '''移动参数'''
        self.xStep = 1
        self.yStep = 1

        # 调用父类
        super(Boss,self).__init__(screen,self.image,self.x,self.y)

    # 2.走一步
    def step(self):
        # 1.坐标修改
        # 1.1 由下往上
        if self.bsIndex == 0:
            self.y -= 2
        # 1.2 修改变量
        if self.y  < -self.height:
            self.bsIndex = 1
        # 1.3 由上往下
        if self.bsIndex == 1:
            if self.x > 512-self.width:
                self.xStep = -1
            if self.x < 0:
                self.xStep = 1
            if self.y < 0:
                self.yStep = 1
            if self.y  > 350:
                self.yStep = -1
            self.x += self.xStep
            self.y += self.yStep


        # 2.动画效果
        self.index += 1
        ix = self.index/10%len(self.images)
        self.image = self.images[self.bsIndex][int(ix)]
