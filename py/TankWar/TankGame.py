'''
TankGame:
1.架构整个框架 630*630
2.绘制背景图
3.地板图
    3.1第一区 二维列表 buildList
    3.2SetImage 添加图片
    3.3第四区域 4.1设置绘制障碍物paintBuild()
4.我方坦克
    4.1 SetImage
    4.2 新建TankObject screen,image,images,x,y
        bliteMe()
    4.3新建MyTank 继承TankObject
    4.4第一区域 设置坦克对象 self.mytank
    4.5第四区域 绘制坦克
    4.6第三区域 键盘监听 对tank进行移动
    4.7MyTank类 新增self.dir 方向值 键盘监听
    4.8添加约束条件 不出界 空白移动


'''
import pygame,sys,random
from TankWar.setImage import SetImage
from TankWar.MyTank import myTank
class TankGame(object):
    #第一区域 变量声明及初始化
    def __init__(self):
        self.screen = pygame.display.set_mode((630,630),0,0)
        self.setImage = SetImage()
        self.buildList = [
            [2, 2, 2, 2, 2, 2 ,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2],
            [1, 1, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ]
        self.mytank_1 = myTank(self.screen,self.setImage.MyTank_1,8*24 + 3,24*24+3)
        self.flag = 0
        # self.mytank_2 = MyTank(self.screen,self.setImage.MyTank_2)
    #第二区域 main函数区域
    def main(self):
        pygame.display.set_caption("坦克大战")
        while True:
            self.screen.blit(self.setImage.backImage,(0,0))
            self.action()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_w] and self.outOfBounds(0, self.mytank_1.x, self.mytank_1.y):
                self.mytank_1.step(0)
            elif key_pressed[pygame.K_s]and self.outOfBounds(1, self.mytank_1.x, self.mytank_1.y):
                self.mytank_1.step(1)
            elif key_pressed[pygame.K_a]and self.outOfBounds(2, self.mytank_1.x, self.mytank_1.y):
                self.mytank_1.step(2)
            elif key_pressed[pygame.K_d]and self.outOfBounds(3, self.mytank_1.x, self.mytank_1.y):
                self.mytank_1.step(3)
            self.paint()
            pygame.display.update()

    #第三区域：业务处理函数
    def action(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pass
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.mytank_1.image = self.setImage.MyTank_1[0]
        elif key_pressed[pygame.K_s]:
            self.mytank_1.image = self.setImage.MyTank_1[1]
        elif key_pressed[pygame.K_a]:
            self.mytank_1.image = self.setImage.MyTank_1[2]
        elif key_pressed[pygame.K_d]:
            self.mytank_1.image = self.setImage.MyTank_1[3]

    #出界函数判断
    def outOfBounds(self,dir,x,y):
        #判断下一步方向
        nX =  int((x-3)/24)
        nY = int((y-3)/24)
        sX = int((x-3)/24)
        sY = int((y-3)/24)

        #根据方向判断下一步
        if dir == 0:
            nY -= 1
            sY -= 1
            sX += 1

        if dir == 1:
            nY += 2
            sY += 2
            sX += 1
        if dir == 2:
            nX -=1
            sY +=1
            sX -=1
        if dir == 3:
            nX += 2
            sX += 2
            sY +=1

            if 0<=nX<=25 and 0<=nY<=25 and 0<=nX<=25 and 0<=nY<=25 and self.buildList[nY][nX] + self.buildList[sY][sX] == 4:
                return True
        return False

    #第四区域：绘制函数
    def paint(self):
        self.paintBuild()
        self.mytank_1.blitMe()
    def paintBuild(self):
        for i in range(0,len(self.buildList)):
            for j in range(0,len(self.buildList[i])):
                type = self.buildList[i][j]
                if type == 2:
                    pass
                else:
                    buildX = 3 + 24*j
                    buildY = 3 + 24*i
                    self.screen.blit(self.setImage.buildImages[type],(buildX,buildY))



if __name__ == '__main__':
    game = TankGame()
    game.main()