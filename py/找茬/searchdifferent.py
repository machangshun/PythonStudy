import pygame,sys,random
class TomCat(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((520,320),0,0)
        self.xx = []
        self.yy = []
        self.ww = []
        self.hh = []
        self.flag = 0
        self.back = pygame.image.load("timg.png")

    def appendrect(self,x,y,w,h):
        self.xx.append(x)
        self.yy.append(y)
        self.ww.append(w)
        self.hh.append(h)
        self.flag += 1
    def main(self):
        pygame.display.set_caption("找茬")
        while True:
            #2.4设置屏幕颜色
            self.screen.fill((255,255,255))
            self.action()
            self.paint()
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
                if 260 < mouseX < 260 + 80 and 180 < mouseY < 180 + 90:
                    self.appendrect(260,180,80,90)
                if 450 < mouseX < 450 + 40 and 70 < mouseY < 70 + 50:
                    self.appendrect(450,70,40,50)
                if 430 < mouseX < 430 + 40 and 250 < mouseY < 250 + 30:
                    self.appendrect(430, 250, 40, 30)
    def paint(self):
        #2.绘制背景
        #图片变形
        self.screen.blit(pygame.transform.scale(self.back,(520,320)),(0,0))
        for i in range(0,self.flag):
            pygame.draw.rect(self.screen, (255, 0, 0), (self.xx[i], self.yy[i], self.ww[i], self.hh[i]), 1)
#        pygame.draw.rect(self.screen, (255, 0, 0), (450,70,40,50), 1)
if __name__ == '__main__':
    cat = TomCat()
    cat.main()