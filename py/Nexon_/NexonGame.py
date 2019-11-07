'''
泡泡堂
1.架构整个项目 925*700
2.绘制背景图
3.地板图
    3.1第一区域 1.3地板图二维列表 floorList
    3.2SetImage 1.2地板图集合
    3.2第四区域 4.1设置绘制地板图函数 paintFloor
4.建筑物图绘制
    4.1第一区域 1.4 建筑物二维列表 buildList
    0 树 1红色模块 2.橙色模块 3.红房子 4.黄房子 5.蓝房子 6.箱子 7.空白
    4.2SetImage 1.3建筑物图集合 build Images
    4.3第四区域 4.2设置建筑物图函数 paintBuild()
5.宝宝移动
    5.1 SetImage 1.4宝宝图集合 baoImages  上下左右
    5.2 新建 NexonObject screen,image,images,x,y
    bliteMe()
    5.3新建Bao 继承与NeoxnObject
    5.4第一区域 1.5设置宝宝对象 self.bao
    5.5第四区域 4.3绘制宝宝
    5.6第三区域 键盘监听 对宝宝进行移动
    5.7Bao类 新增 self.dir 方向值 键盘监听
    5.8添加约束条件 不出界 空白移动
6.泡泡
    6.1新建类 继承NexonObject
    6.2第一区域 声明变量 self.paos = []
    6.3第三区域 键盘J 添加泡泡对象到paos中
    6.4第四区域 添加函数paintPaos() 循环遍历 绘制自己
    6.5第三区域 新建stepAction函数 被调用
    6.6第三区域 stepAction函数 调用泡泡类下方的step函数
        动画效果
    6.7Pao类 添加属性 self.life = 88
            添加修改生命值
            第三区域 stepAction调用 subLife
7.炸弹
    7.1新建 Bomb类 继承于NexonObject
    7.2第一区域 声明变量 self.bombs = []
    7.3 第三区域 3.5stepAction函数 调用createBomb函数（pao.row,pao.col）
    7.4第三区域 3.5.1createBomb函数 添加5颗炸弹
    7.5第四区域 绘制炸弹 paintBomb调用
    7.6第三区域 3.5stepAction函数 循环遍历所有的炸弹 并将炸弹进行生命值消失 self.life = 38 调用bomb类中step函数
1.处理炸弹出界问题
2.处理不可炸建筑物类型
    0 3 4 5 不可炸建筑物类型
    1 2 6 7 可炸建筑物类
8.建筑物消失
    根据炸弹的位置修改buildList
9.销毁
    9.1新建销毁类Destroy 类 继承NexonObject
    9.2第一区域 声明变量 self.destroys = []
    9.3第三区域 炸弹销毁建筑物的时候 1，2，6 添加销毁
        炸弹消失时 提前判断建筑物类型 若建筑物类型是1，2，6则添加销毁对象
    9.4第四区域 绘制销毁对象 paintDestroy()
    9.5第三区域 3.5stepAction 调用Destroy类中 step函数
        life ==>80-60 绘制第一张图 60-40 绘制第二张 40-20 第三张
10.道具
    10.1新建道具类 Prop类 继承 NexonObject
    10.2第一区域 声明变量 self.props = []
    10.3第三区域 3.5 stepAction 销毁对象死亡
        添加道具对象
    10.4第四区域 绘制道具 paintProp()
    10.5第三区域 键盘监听最后 添加函数 coinsice(bRow,bCol)
        跟道具对象进行 遍历 判断
        删除道具 增加宝宝的属性值
    10.6Bao类中 添加三个属性
        self.speed = 1
        self.number = 1
        self.power = 1
    10.7添加道具效果

11.推箱子
12.泡泡阻挡游戏

课后作业：
1.海海 上下移动
'''
import pygame,sys,random
from Nexon_.Bao import Bao
from Nexon_.SetImage import SetImage
from Nexon_.haihai import Hai
from Nexon_.Pao import Pao
from Nexon_.Bomb import Bomb
from Nexon_.Destroy import Destory
from Nexon_.Prop import Prop
class NexonGame(object):
    '''第一区域变量声明区域'''
    def __init__(self):
        self.screen = pygame.display.set_mode((925,700),0,0)
        #设置图片加载类
        self.setImage = SetImage()
        #设置地板图二维列表
        self.floorList = [
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0]
        ]
        self.buildList = [
            [7, 2, 1, 2, 1, 0, 7, 7, 6, 0, 5, 1, 5, 7, 5],
            [7, 3, 6, 3, 7, 0, 6, 7, 7, 0, 1, 2, 7, 7, 7],
            [7, 7, 2, 1, 2, 0, 7, 6, 6, 0, 5, 6, 5, 6, 5],
            [6, 5, 6, 5, 6, 0, 6, 7, 7, 0, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 1, 7, 7, 6, 0, 5, 6, 5, 6, 5],
            [2, 3, 2, 3, 2, 3, 6, 6, 7, 7, 1, 2, 1, 2, 1],
            [0, 0, 0, 0, 0, 0, 7, 7, 6, 0, 0, 0, 0, 0, 0],
            [1, 2, 1, 2, 1, 7, 6, 7, 7, 2, 1, 3, 1, 3, 7],
            [4, 6, 4, 6, 4, 0, 7, 6, 6, 0, 2, 1, 2, 7, 7],
            [2, 1, 2, 1, 2, 0, 6, 7, 7, 0, 6, 3, 6, 3, 7],
            [4, 7, 4, 6, 4, 0, 7, 7, 6, 0, 1, 2, 1, 2, 7],
            [7, 7, 1, 2, 1, 0, 6, 6, 7, 0, 6, 3, 7, 3, 7],
            [4, 7, 4, 1, 4, 0, 7, 7, 6, 0, 2, 7, 7, 7, 7]
        ]
        #设置宝宝对象
        self.bao = Bao(self.screen,self.setImage.baoImages)
        self.hai = Hai(self.screen,self.setImage.haiImages)
        self.paos = []
        self.bombs = []
        self.destroys = []
        self.props = []
    '''第二区域：main函数区域'''
    def main(self):
        pygame.display.set_caption("泡泡堂")
        while True:
            self.screen.blit(self.setImage.backImage,(0,0))
            #调用业务
            self.action()
            self.paint()
            pygame.display.update()
    '''第三区域：业务处理'''
    def action(self):
        #循环遍历所有监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #判断比较
                #上
                if event.key == pygame.K_w and self.outOfBounds(0,self.bao.row,self.bao.col):
                    self.bao.step(0)
                if event.key == pygame.K_s and self.outOfBounds(1,self.bao.row,self.bao.col):
                    self.bao.step(1)
                if event.key == pygame.K_a and self.outOfBounds(2,self.bao.row,self.bao.col):
                    self.bao.step(2)
                if event.key == pygame.K_d and self.outOfBounds(3,self.bao.row,self.bao.col):
                    self.bao.step(3)
                if event.key == pygame.K_UP and self.outOfBounds(0,self.hai.row,self.hai.col):
                    self.hai.step(0)
                if event.key == pygame.K_DOWN and self.outOfBounds(1,self.hai.row,self.hai.col):
                    self.hai.step(1)
                if event.key == pygame.K_LEFT and self.outOfBounds(2,self.hai.row,self.hai.col):
                    self.hai.step(2)
                if event.key == pygame.K_RIGHT and self.outOfBounds(3,self.hai.row,self.hai.col):
                    self.hai.step(3)
                if event.key == pygame.K_j and self.bao.number >= 1:
                    self.bao.number -= 1
                    self.paos.append(Pao(self.screen,self.setImage.paoImages,self.bao.row,self.bao.col))
                if event.key == pygame.K_RETURN:
                    self.paos.append(Pao(self.screen,self.setImage.paoImages,self.hai.row,self.hai.col))
        self.stepAction()
        self.coinside(self.bao.row,self.bao.col)
        self.coinside(self.hai.row,self.hai.col)
    #3.4宝宝出界函数
    def outOfBounds(self,dir,row,col):
        #判断下一步方向
        nextRow = row
        nextCol = col
        #根据方向判断下一步
        if dir == 0:
            nextRow -= 1
        if dir == 1:
            nextRow += 1
        if dir == 2:
            nextCol -= 1
        if dir == 3:
            nextCol += 1
        #判断是否出界
        '''宝宝建筑物类型判断
        '''
        if 0<=nextRow<=12 and 0<=nextCol<=14:
            type = self.buildList[nextRow][nextCol]
            return type == 7
        return False
    def stepAction(self):
        for pao in self.paos:
            pao.step()
            #判断生命值
            if pao.life < 0:
                self.createBomb(pao)
                self.paos.remove(pao)
                self.bao.number += 1
        for bomb in self.bombs:
            bomb.step()
            if bomb.life < 0:
                self.buildList[bomb.row][bomb.col] = 7
                self.bombs.remove(bomb)
        for dis in self.destroys:
            dis.step()
            if dis.life < 0:
                randType = random.randint(0,20)
                if randType < 15:
                    self.props.append(Prop(self.screen, self.setImage.propImages, dis.row, dis.col))
                self.destroys.remove(dis)
    def coinside(self,bRow,bCol):
        for pro in self.props:
            if pro.row == bRow and pro.col == bCol:
                if pro.num == 0:
                    self.bao.speed += 1
                elif pro.num == 1:
                    self.bao.power += 1
                else:
                    self.bao.number += 1
                self.props.remove(pro)

    def createBomb(self,pao):
        row = pao.row
        col = pao.col
        if self.judgeType(row,col):
            self.bombs.append(Bomb(self.screen,self.setImage.bombImages[0],row,col))
        for i in range(1,self.bao.power+1):
            if pao.DOWN and self.judgeType(row + i, col):
                self.bombs.append(Bomb(self.screen, self.setImage.bombImages[0], row + i, col))
                if self.judgeBuildType(row + i, col):
                    self.destroys.append(Destory(self.screen, self.setImage.destoryImages, row + i, col))
            elif pao.DOWN and self.judgeType2(row+i,col):
                pao.DOWN = False
            if self.judgeType(row - i, col) and pao.UP:
                self.bombs.append(Bomb(self.screen, self.setImage.bombImages[0], row - i, col))
                if self.judgeBuildType(row - i, col):
                    self.destroys.append(Destory(self.screen, self.setImage.destoryImages, row - i, col))
            elif pao.UP and self.judgeType2(row-i,col):
                pao.UP = False
            if self.judgeType(row, col + i) and pao.RIGHT:
                self.bombs.append(Bomb(self.screen, self.setImage.bombImages[1], row, col + i))
                if self.judgeBuildType(row, col + i):
                    self.destroys.append(Destory(self.screen, self.setImage.destoryImages, row, col + i))
            elif pao.RIGHT and self.judgeType2(row,col+i):
                pao.RIGHT = False
            if self.judgeType(row, col - i) and pao.LEFT:
                self.bombs.append(Bomb(self.screen, self.setImage.bombImages[1], row, col - i))
                if self.judgeBuildType(row, col - i):
                    self.destroys.append(Destory(self.screen, self.setImage.destoryImages, row, col - i))
            elif pao.LEFT and self.judgeType2(row,col-i):
                pao.LEFT = False

    def judgeType(self,bRow,bCol):
        if  0<=bRow<= 12 and 0 <= bCol <= 14:
            type = self.buildList[bRow][bCol]
            return type in [1,2,6,7]
        return False
    def judgeType2(self,bRow,bCol):
        if 0<= bRow<=12 and 0<=bCol<=14:
            type = self.buildList[bRow][bCol]
            return type in [0,3,4,5]
        return False
    def judgeBuildType(self,bRow,bCol):
        if 0<=bRow<= 12 and 0 <= bCol <= 14:
            type = self.buildList[bRow][bCol]
            return type in [1,2,6]
        return False
    '''第四区域：绘制'''
    def paint(self):
        #绘制地板图函数
        self.paintFloor()
        self.paintBuild()
        self.bao.blitMe()
        self.hai.blitMe()
        self.paintPaos()
        self.paintBomb()
        self.paintDestroy()
        self.paintProp()
    def paintFloor(self):
        #所有元素进行遍历
        for i in range(0,len(self.floorList)):
            for j in range(0,len(self.floorList[i])):
                type = self.floorList[i][j]
                floorX = 25 + 50*j
                floorY = 25 + 50 *i
                self.screen.blit(self.setImage.floorImages[type],(floorX,floorY))
    def paintBuild(self):
        for i in range(0,len(self.buildList)):
            for j in range(0,len(self.buildList[i])):
                type = self.buildList[i][j]
                if type == 7:
                    pass
                else:
                    floorX = 25 + 50 * j
                    floorY = 25 + 50 * i
                    self.screen.blit(self.setImage.buildImages[type], (floorX, floorY))
    def paintPaos(self):
        for pao in self.paos:
            pao.blitMe()
    def paintBomb(self):
        for bomb in self.bombs:
            bomb.blitMe()
    def paintDestroy(self):
        for dis in self.destroys:
            dis.blitMe()

    def paintProp(self):
        for pro in self.props:
            pro.blitMe()
if __name__ == '__main__':
    game = NexonGame()
    game.main()