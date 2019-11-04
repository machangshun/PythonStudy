'''
1.架构项目
2.背景图
    2.1第一区域 声明变量back
    2.2第四区域 绘制背景
3.帧动画
    3.1第一区域 列表存储所有的图片
    3.2第一区域 设置列表下表值
    3.3第五区域 initImage==>遍历图片返回给列表
    3.4第三区域 设置index的值
4.设置按钮图片
    4.1第一区域 设置变量 self.eat
    4.2第四区域 绘制吃鸟图片
    4.3第三区域 监听事件下方 鼠标监听
                判断是否点击
    4.4第一区域 设置变量 self.count
'''
'''
课堂练习和课后作业
1.完成6套带有图片的动画
2.完成5套动作
'''
import pygame,sys,random
class TomCat(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((320,512),0,0)
        #背景
        self.back = pygame.image.load("Animations/Eat/eat_00.jpg")
        #图片列表 40张图片路径
        self.images = []
        #1.4 设置图片集转换值
        self.index = 0
        self.eat = pygame.image.load("Buttons/eat.png")
        self.cymbal = pygame.image.load("Buttons/cymbal.png")
        self.drink = pygame.image.load("Buttons/drink.png")
        self.fart = pygame.image.load("Buttons/fart.png")
        self.pie = pygame.image.load("Buttons/pie.png")
        self.scratch = pygame.image.load("Buttons/scratch.png")
        #设置吃鸟图片集转换值
        self.count = -1
    def main(self):
        pygame.display.set_caption("汤姆猫")
        while True:
            #2.4设置屏幕颜色
            self.screen.fill((255,255,255))
            self.action()
            self.paint()
            pygame.time.delay(10)
            pygame.display.update()
    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #3.6鼠标监听
            if event.type == pygame.MOUSEBUTTONDOWN:
                #3.7获取鼠标坐标值
                mouseX,mouseY = pygame.mouse.get_pos()
                #3.8判断是否点击了吃鸟的动作
                if 10 < mouseX < 10 + 60 and 140 < mouseY < 140 + 60:
                    #3.9设置统计数
                    self.count = 12
                    self.initImages("cymbal")
                elif 10 < mouseX < 70 and 200 < mouseY < 260:
                    self.count = 80
                    self.initImages("drink")
                elif 10 < mouseX < 70 and 260 < mouseY < 320:
                    self.count = 39
                    self.initImages("eat")
                elif 10 < mouseX < 70 and 320 < mouseY < 380:
                    self.count = 27
                    self.initImages("fart")
                elif 10 < mouseX < 70 and 380 < mouseY < 440:
                    self.count = 23
                    self.initImages("pie")
                elif 10 < mouseX < 70 and 440 < mouseY < 500:
                    self.count = 55
                    self.initImages("scratch")
                elif 80 < mouseX < 80+170 and 100 < mouseY < 100 + 150:
                    self.count = 80
                    self.initImages("knockout")
                elif 120 < mouseX < 120 + 70 and 380 < mouseY < 380 + 70:
                    self.count = 33
                    self.initImages("stomach")
                elif 110 < mouseX < 110 + 40 and 460 < mouseY < 460 + 40:
                    self.count = 29
                    self.initImages("footright")
                elif 160 < mouseX < 160+40 and 460 < mouseY < 460 + 40:
                    self.count = 29
                    self.initImages("footleft")
                elif 210 < mouseX < 210+40 and 410 < mouseY < 410 + 50:
                    self.count = 25
                    self.initImages("angry")
        #3.3设置背景图
        #每运行一次 index就变化一次
        '''
        核心代码
        '''
        if self.count > self.index:
            self.index += 1
            self.back = pygame.image.load(self.images[self.index])
        else:
            #修改变量
            self.count = -1
            self.index = 0
            #删除列表所有元素
            self.images.clear()

    def paint(self):
        #2.绘制背景
        #图片变形
        self.screen.blit(pygame.transform.scale(self.back,(320,512)),(0,0))
        #4.2绘制吃鸟图片
        self.screen.blit(self.cymbal, (10, 140))
        self.screen.blit(self.drink,(10,200))
        self.screen.blit(self.eat,(10,260))
        self.screen.blit(self.fart,(10,320))
        self.screen.blit(self.pie,(10,380))
        self.screen.blit(self.scratch,(10,440))

        # pygame.draw.rect(self.screen,(255,0,0),(80,100,170,150),1)
        # pygame.draw.rect(self.screen,(255,0,0),(120,380,70,70),1)
        # pygame.draw.rect(self.screen, (255, 0, 0), (110,460, 40,40), 1)
        # pygame.draw.rect(self.screen, (255, 0, 0), (160,460, 40,40), 1)
        # pygame.draw.rect(self.screen, (255, 0, 0), (210,410, 40,50), 1)
    def initImages(self,flag):
        for i in range(0, self.count + 1):
            self.images.append("Animations/%s/%s_%02d.jpg" %(flag.capitalize(),flag,i))

if __name__ == '__main__':
    cat = TomCat()
    cat.main()