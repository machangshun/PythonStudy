'''
1. 搭建项目框架
2. 背景图
3. 地板图
    3.1 Setting类中设置地板图图片
    3.2 Setting类中设置地板坐标值
        二维列表 floorMap=[[]]
    3.3 NexonGame 中， 第四区域paint
        绘制地板 4.1 paintFloor()
4. 建筑物图片
    4.1 Setting 类中设置建筑物图片
    4.2 NexonGame类中 第一区域
        BulidMap=[[]]
        0 代表树
        1 代表红色模块
        2 代表橙色模块
        3 代表红房子
        4 代表黄房子
        5 代表蓝房子
        6 代表箱子
        7 空白
    4.3 NexonGame 类中  第四区域
        4.2 paintBuild()
5. 宝宝
    5.1 新建BaoBao类 上下左右0，1，2，3
    5.2 父类NexoObject类
        screen，image，row，col
        step函数
        outOfBounds()函数
    5.3 第一区域 初始化宝宝类
    5.4 第四区域，绘制宝宝
    5.5 宝宝移动
        第三区域 判断是否点击键盘

6. 泡泡
    6.1 新建PaoPao类，继承NexonObject
    Setting 两张图片 图片paoImages

    animation()
    6.2 NexonGame类 第一区域
    self.paos = []
    6.3 NexonGame 第三区域  J
    paos.append(PaoPao(self.screen, self.bao.row, self.bao.col, self.setting.paoImages))
    6.4 第三区域下方写animateAction()
        遍历所有的泡泡 调用animation()

'''
import pygame, sys
from Nexon.setting import Setting
from Nexon.BaoBao import BaoBao
from Nexon.PaoPao import PaoPao
from Nexon.Bomb import Bomb
from Nexon.Distory import Distory

class NexonGame(object):
    '''第一区域'''
    def __init__(self):
        # 屏幕
        self.screen = pygame.display.set_mode((925, 700), 0 ,0)
        # 初始化Setting类
        self.setting = Setting()

        # 地板图二位列表 13行 15列
        self.floorMap = [
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

        # 建筑物
        self.buildMap = [
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

        self.bao = BaoBao(self.screen, self.setting.baoImages)

        # 泡泡列表
        self.paos = []

        # bomb列表
        self.bombs = []

        # 损坏
        self.distorys = []
    '''第二区域'''
    def menu(self):
        pygame.display.set_caption("泡泡堂")
        while True:
            # 背景
            self.screen.blit(self.setting.back, (0, 0))
            # 调用action函数
            self.action()
            # 调用paint函数
            self.paint()
            # 刷新屏幕
            pygame.display.update()

    '''第三区域'''
    def action(self):
        # 遍历所有的监听时间
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.step(0)
                elif event.key == pygame.K_s:
                    self.step(1)
                elif event.key == pygame.K_a:
                    self.step(2)
                elif event.key == pygame.K_d:
                    self.step(3)
                elif event.key == pygame.K_j:
                    self.paos.append(PaoPao(self.screen, self.bao.row, self.bao.col, self.setting.paoImages))

        self.animateAction()

    def animateAction(self):
        for pao in self.paos:
            pao.animation()
            if pao.life < 0:
                self.bombs.append(Bomb(self.screen, pao.row + 1, pao.col, self.setting.bomb1))
                self.bombs.append(Bomb(self.screen, pao.row - 1, pao.col, self.setting.bomb1))
                self.bombs.append(Bomb(self.screen, pao.row, pao.col - 1, self.setting.bomb2))
                self.bombs.append(Bomb(self.screen, pao.row, pao.col + 1, self.setting.bomb2))
                self.paos.remove(pao)

        for bomb in self.bombs:
            if 0 <= bomb.row <= 12 and  0<= bomb.col <= 14 and self.buildMap[bomb.row][bomb.col] == 7:
                bomb.bombing()
                if bomb.life < 0:
                    self.bombs.remove(bomb)
            elif 0 <= bomb.row <= 12 and  0<= bomb.col <= 14 and self.buildMap[bomb.row][bomb.col] != 7:
                self.bombs.remove(bomb)
                self.buildMap[bomb.row][bomb.col] = 7
                self.distorys.append(Distory(self.screen, bomb.row, bomb.col, self.setting.distoryImages))
        for dis in self.distorys:
            dis.animation()
            if dis.life < 0:
                self.distorys.remove(dis)


    # 宝宝移动函数
    def step(self, dir):
        # 上下左右 0，1，2，3
        if dir == 0 and self.outOfBound(dir):
            self.bao.row -= 1
        elif dir == 1 and self.outOfBound(dir):
            self.bao.row += 1
        elif dir == 2 and self.outOfBound(dir):
            self.bao.col -= 1
        elif dir == 3 and self.outOfBound(dir):
            self.bao.col += 1
        self.bao.image = self.bao.images[dir]

    # 宝宝出界函数
    def outOfBound(self, dir):
        bRow = -1
        bCol = -1
        # 上下左右
        if dir == 0:
            bRow = self.bao.row - 1
            bCol = self.bao.col
        elif dir == 1:
            bRow = self.bao.row + 1
            bCol = self.bao.col
        elif dir == 2:
            bCol = self.bao.col - 1
            bRow = self.bao.row
        elif dir ==  3:
            bCol = self.bao.col + 1
            bRow = self.bao.row
        # 13行， 15列， （0，12），（0，14）

        # 判断宝宝下一步所在建筑物类型

        return 0 <= bRow <= 12 and  0<= bCol <= 14 and self.buildMap[bRow][bCol] == 7

    '''第四区域'''
    def paint(self):
        # 绘制地板图
        self.paintFloor()
        # 绘制建筑物
        self.paintBuild()
        # 绘制宝宝
        self.bao.blitMe()
        # 绘制泡泡
        self.paintPao()
        # 绘制爆炸
        self.paintBomb()
        # 绘制爆炸
        self.paintDistory()

    def paintFloor(self):
        for i in range(len(self.floorMap)):
            for j in range(len(self.floorMap[i])):
                # 设置坐标值
                floodx = 25 + j*50
                floody = 25 + i*50
                # 判断处理
                type = self.floorMap[i][j]
                typeImage = None
                if type == 0:
                    typeImage = self.setting.diban0
                elif type == 1:
                    typeImage = self.setting.diban1
                elif type == 2:
                    typeImage = self.setting.diban2
                self.screen.blit(typeImage, (floodx, floody))

    def paintBuild(self):
        for i in range(len(self.buildMap)):
            for j in range(len(self.buildMap[i])):
                # 设置坐标值
                buildx = 25 + j*50
                buildy = 25 + i*50
                # 判断处理
                type = self.buildMap[i][j]
                typeImage = None
                if type == 0:
                    typeImage = self.setting.house0
                elif type == 1:
                    typeImage = self.setting.house1
                elif type == 2:
                    typeImage = self.setting.house2
                elif type == 3:
                    typeImage = self.setting.house3
                elif type == 4:
                    typeImage = self.setting.house4
                elif type == 5:
                    typeImage = self.setting.house5
                elif type == 6:
                    typeImage = self.setting.house6
                if type != 7:
                    self.screen.blit(typeImage, (buildx, buildy))

    def paintPao(self):
        for pao in self.paos:
            pao.blitMe()

    def paintBomb(self):
        for bomb in self.bombs:
            if 0 <= bomb.row <= 12 and 0 <= bomb.col <= 14 :
                bomb.blitMe()

    def paintDistory(self):
        for dis in self.distorys:
            dis.blitMe()

if __name__ == '__main__':
    game = NexonGame()
    game.menu()
