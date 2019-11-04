'''
打字游戏
1.随机参生字符
2.键盘监听事件判断
完成以下功能：
1.字符由上往下落
2.字符与键盘监听事件进行比较判断
3.若键盘输入了该字符则进行覆盖 生成其他字符 再随机坐标值
4.加分 击中一个字符加5分 并将分数显示出来
'''
'''
作业：
1.字符五颜六色
2.根据分数调整速度
    100以内 20
    200以内 15
    300     10
    400     5
    500     1
3.字符超过下边界 分数减少10分
'''
import pygame,sys,random
class MyWord(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600),0,0)
        self.words = []
        self.x = []
        self.y = []
        self.score = 0
        self.color = []
        self.speed = 20
        for i in range(0,10):
            self.words.append(random.randint(65,90))
            self.x.append(random.randint(0,800-28))
            self.y.append(-random.randint(0,600-28))
            self.color.append(self.getcolor())

    def getcolor(self):
        R  = random.randint(0,254)
        G = random.randint(0,254)
        B = random.randint(0,254)
        return R,G,B

    def main(self):
        pygame.display.set_caption("打字游戏")
        while True:
            self.screen.fill((255,255,255))
            self.action()
            self.paint()
            pygame.time.delay(self.speed)
            pygame.display.update()

    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #键盘监听
            if event.type == pygame.KEYDOWN:
                for i in range(0,len(self.words)):
                    #python中默认比较小写字符
                    if event.key == self.words[i]+32 and self.y[i]>0:
                        self.words[i] = random.randint(65,90)
                        self.x[i] = random.randint(0,800-28)
                        self.y[i] = -random.randint(0,600-28)
                        self.color[i] = self.getcolor()
                        self.score += 5
                        break

        for ix in range(0,10):
            self.y[ix] += 1
            if self.y[ix] > 600:
                self.y[ix] = 0
                self.score -= 10
        if self.score > 100:
            self.speed = 15
        if self.score > 200:
            self.speed = 10
        if self.score > 300:
            self.speed = 5
        if self.score > 400:
            self.speed = 1
    def paint(self):
        pygame.font.init()
        font = pygame.font.Font("simkai.ttf",28)
        fontRead1 = font.render("score:%d"%self.score, True, (0, 0, 0))
        self.screen.blit(fontRead1, (10, 10))
        for i in range(0,len(self.words)):
            fontRead = font.render(chr(self.words[i]), True, self.color[i])
            self.screen.blit(fontRead, (self.x[i], self.y[i]))

if __name__ == '__main__':
    word = MyWord()
    word.main()