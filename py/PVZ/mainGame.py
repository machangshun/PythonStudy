'''
mainGame
1.架构整个项目 1400*600
2.绘制背景
3.绘制太阳
    3.1 initSun()
    3.2 setImage
    3.3 paintSun()
4.植物类
5.子弹
6.僵尸类
7.碰撞

'''

import pygame, sys, random
from  pygame.locals import *
from setImage import setImage
from Sun import Sun
from Para import Para
#植物类
from plant.sunflower import Sunflower
from plant.peashooter import Peashooter
from plant.cherryBomb import CherryBomb
from plant.repeater import Repeater
from plant.cactus import Cactus
from plant.wallnut import Wallnut
from bullet import Bullet
#僵尸类
from zombie.zombie_bucket import Zombie_bucket
from zombie.zombie_conehead import Zombie_conehead
from zombie.zombie_normal import Zombie_normal
from zombie.zombie_head import Zombie_head
from zombie.zombie_dead import Zombie_dead

sets = setImage()
para = Para
screen = pygame.display.set_mode((1400, 600), 0, 0)
class mainGame(object):
    def __init__(self):
        # 用于表示是否选择了卡片
        para.cardState = para.CARD_NOT_CLICKED
        # 表示选择卡片的类型
        para.cardSelection = para.NUT_SELECTED
        # 表示当前需要绘制的图片
        para.paintPlants = []
        # 僵尸存储列表
        para.zombies = []
        # 僵尸频率值
        para.zombieIndex = 0
        # 掉头信号
        para.headFlag = True
        para.zombieRate = 0
        # 存放正在下落太阳的列表
        para.sunFall = []
        # 存放已经停止的太阳的列表
        para.sunStay = []
        for i in range(1):
            xx = random.randint(260, 880)
            yy = -random.randint(100, 300)
            goal = random.randint(300, 600)
            sun = Sun(screen, sets.sunImage, xx, yy, goal)
            para.sunFall.append(sun)
        # 记录初始阳光数的
        para.sunScore = 200
        # 全局统一的时间轴
        para.globalTime = 0
        # 格子的二维数组
        para.gridList = [([-1] * 5) for i in range(9)]
        # 游戏状态
        para.state = 0
        # 子弹存储列表
        para.bullets = []
        #僵尸列表
        para.zombies = []
        # 植物频率值
        para.plantIndex = 0
        # 子弹生成频率值
        para.shootIndex = 0
        # 游戏结束信号
        para.endFlag = 0

    def initSun(self):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy, goal)
        para.sunFall.append(sun)
    def main(self):
        pygame.display.set_caption("植物大战僵尸")
        self.initSun()
        while True:
            self.action()
            self.paint()
            pygame.display.update()

    # 业务逻辑主函数
    def action(self):
        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.initPlantsMouseClickListener()
                self.cardMouseClickListener()
                self.sunMouseClickListener()
                self.runOrPause()
        if para.state == para.RUNNING:
            self.stepAction()
            #生成僵尸
            self.zombiesAction()
            # 阳光的动作
            self.sunAction()
            # 控制全局的时间轴时间增加
            para.globalTime += 2
            self.hitAction()
            self.endAction( screen, sets)

    def stepAction(self):
        for plant in para.paintPlants:
            plant.step()
        # 僵尸走一步
        for zombie in para.zombies:
            zombie.step(sets)
        # 子弹走一步
        for bullet in para.bullets:
            bullet.step()
            if bullet.outOfBounds():
                para.bullets.remove(bullet)

    # 生成阳光
    def sunAction(self):
        for i in range(len(para.sunFall)):
            para.sunFall[i].step()
            # 阳光落到地上后，生成新的下落阳光
            if para.sunFall[i].index == para.sunFall[i].goal:
                para.sunStay.append(para.sunFall[i])
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                para.sunFall[i] = Sun(screen, sets.sunImage, xx, yy, goal)
                break
        # 掉在地上的阳光如果不去点击收集，过一段时间会自动消失
        for i in range(len(para.sunStay)):
            para.sunStay[i].disappearTime += 1
        for i in range(len(para.sunStay)):
            if para.sunStay[i].disappearTime == 200:
                del para.sunStay[i]
                break

    # 僵尸生成
    def zombiesAction(self):
        para.zombieIndex += 1
        if 7000 <= para.globalTime <= 8000 or 14200 <= para.globalTime <= 14400:
            para.zombieRate = 50
        else:
            para.zombieRate = 500

        if para.globalTime == 14300:
            para.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
            para.endFlag = 1
        if para.globalTime < 14400:
            if para.zombieIndex % para.zombieRate == 0:
                type = random.randint(0, 20)
                if type < 8:
                    para.zombies.append(Zombie_conehead(screen, sets.zombie_coneheadImages))
                else:
                    # 存储到列表中
                    para.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))

    # 子弹碰撞僵尸
    def hitAction(self):
        for zombie in para.zombies:
            self.eat(zombie)
            self.hit(zombie)
            if zombie.life == 5:
                if not isinstance(zombie, Zombie_normal):
                    zombie.images = sets.zombie_normalImages
            elif zombie.life <= 0:
                if zombie.headFlag is True:
                    zombie.images = sets.zombieLostHeadImages
                    zombie.headFlag = False
                    para.zombies.remove(zombie)

    # 僵尸吃植物
    def eat(self, zb):
        for plant in para.paintPlants:
            if not (isinstance(plant, CherryBomb) or isinstance(zb, Zombie_head) or isinstance(zb, Zombie_dead)):
                if plant.x + plant.width - 30 < zb.x < plant.x + plant.width - 10 and plant.y - 100 < zb.y < plant.y:
                    if zb.life <= 0:
                        zb.images = sets.zombieDieImages
                        para.zombies.remove(zb)
                    elif 0 < zb.life <= 5:
                        zb.images = sets.normalAttackImages
                    elif 5 < zb.life <= 8:
                        if not isinstance(zb, Zombie_bucket):
                            zb.images = sets.coneheadAttackImages
                        else:
                            zb.images = sets.bucketAttackImages
                    else:
                        zb.images = sets.bucketAttackImages
                    plant.life -= 0.5
                    if plant.life == 0:
                        para.gridList[plant.gridX][plant.gridY] = -1
                        para.paintPlants.remove(plant)
                        if zb.images == sets.normalAttackImages:
                            zb.images = sets.zombie_normalImages
                        elif zb.images == sets.coneheadAttackImages:
                            zb.images = sets.zombie_coneheadImages
                        else:
                            zb.images = sets.zombie_bucketImages

    # 僵尸被攻击
    def hit(self, zombie):
        for bt in para.bullets:
            if zombie.hitBy(bt):
                if bt.type == 1:
                    zombie.life -= 2
                elif bt.type == 0:
                    zombie.life -= 1
                if zombie.life == 5:
                    if not isinstance(zombie, Zombie_normal):
                        zombie.images = sets.zombie_normalImages
                elif zombie.life <= 0:
                    if zombie.headFlag is True:
                        zombie.images = sets.zombieLostHeadImages
                        para.zombies.append(Zombie_head(screen, sets.zombieHeadImages, zombie.x, zombie.y))
                        para.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))
                para.bullets.remove(bt)

    def endAction(self, screen, sets):
        if para.endFlag == 1 and len(para.zombies) == 0:
            para.state = para.END
            return
        for zombie in para.zombies:
            if zombie.outOfBounds():
                para.state = para.DEAD
                break


    # 场景绘制主函数
    def paint(self):
        if para.state == para.START:
            self.initStartSurface()
            return
        # 判断是否需要画暂停标志
        self.initScenario()
        self.paintZombie()
        self.cardMovePaint()
        self.paintPlant()
        self.paintBullets()
        # 绘制下落及在地上的太阳
        self.paintSun(screen, sets)
        # 绘制太阳总分数状态
        self.paintSunScore(screen, sets)
        # 绘制进度条
        self.painProgressBar(screen, sets)
        if para.state == para.PAUSE:
            self.paintPause()
        elif para.state == para.DEAD:
            self.deadPaint(screen, sets)
        elif para.state == para.END:
            self.wonPaint(screen, sets)
    # 绘制僵尸
    def paintZombie(self):
        for zombie in para.zombies:
            zombie.blitme()
            if isinstance(zombie, Zombie_head) or isinstance(zombie, Zombie_dead):
                if zombie.reloadFlag == 1:
                    para.zombies.remove(zombie)
    # 绘制植物
    def paintPlant(self):
        for plant in para.paintPlants:
            plant.blitme()
    # 绘制子弹
    def paintBullets(self):
        for bullet in para.bullets:
            bullet.blitme()
    # 卡片图标鼠标跟随绘制
    def cardMovePaint(self):
        if para.cardState == para.CARD_CLICKED:
            dict = {
                para.NUT_SELECTED: 0,
                para.SUNFLOWER_SELECTED: 1,
                para.PEASHOOTER_SELECTED: 2,
                para.CHOMPER_SELECTED: 3,
                para.CHERRY_SELECTED: 4,
                para.REPEATER_SELECTED: 5,
                para.SHOVEL_SELECTED: 6
            }
            drawImgIdx = dict[para.cardSelection]
            mousex, mousey = pygame.mouse.get_pos()
            screen.blit(sets.cardImgs[drawImgIdx], (mousex - 27, mousey - 34))
    # 初始场景绘制
    def initScenario(self):
        screen.blit(sets.background, (0, 0))
        screen.blit(sets.seedBank, (0, 0))
    # 绘制卡片
        CARD_OFFSET = 60
        dict = {
            0: sets.cardNutWall,
            1: sets.sunflower,
            2: sets.cardPeashooter,
            3: sets.cactus,
            4: sets.cherry,
            5: sets.cardPeashooterdouble
        }
        dictDark = {
            0: sets.cardNutWallDark,
            1: sets.sunflowerDark,
            2: sets.cardPeashooterDark,
            3: sets.cactusDark,
            4: sets.cherryDark,
            5: sets.cardPeashooterdoubleDark
        }
        for i in range(6):
            if i <= 1 and para.sunScore >= 50:
                screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
            elif  1 < i <= 2 and para.sunScore >= 100:
                screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
            elif 2 < i <= 3 and para.sunScore >= 125:
                screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
            elif 3 < i <= 4 and para.sunScore >= 150:
                screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
            elif 4 < i <= 5 and para.sunScore >= 200:
                screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
            else:
                screen.blit(dictDark[i], (80 + CARD_OFFSET * i, 10))
        screen.blit(sets.cardShovelBack, (448, 0))
        screen.blit(sets.cardShovel, (444, 10))
        # 绘制暂停按钮
        screen.blit(sets.Button, (1265, 10))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 28)
        Str = ft.render("暂 停", True, (0, 0, 0))
        screen.blit(Str, (1290, 14))
    # 绘制太阳，包括在正在下落的和在地上的
    def paintSun(self, screen, sets):
        for i in range(len(para.sunFall)):
            para.sunFall[i].blitme()
        for i in range(len(para.sunStay)):
            para.sunStay[i].blitme()
    # 绘制阳光数
    def paintSunScore(self, screen, sets):
        pygame.font.init()
        ft = pygame.font.Font('msyh.ttf', 20)
        scoreStr = ft.render("%d"%para.sunScore, True, (0, 0, 0))
        if para.sunScore <= 1000:
            screen.blit(scoreStr, (19, 59))
        else:
            screen.blit(scoreStr, (17, 59))
    # 绘制进度条
    def painProgressBar(self, screen, sets):
        # 绘制进度条
        percentage = para.globalTime / 100
        # 绘制开始提示标语
        if 1 <= percentage <= 2:
            screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 0), (255, 112))), (550, 240))
        if 2 <= percentage <= 3:
            screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 112), (255, 100))), (550, 240))
        if 3 <= percentage <= 4:
            screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 212), (255, 112))), (550, 240))
        # 绘制一大波僵尸提示语
        if 70 <= percentage <= 80:
            screen.blit(sets.largeWave, (525, 240))
        # 绘制最后一波提示语
        if 143 <= percentage <= 144:
            screen.blit(sets.finalWave, (525, 240))
        screen.blit(sets.flagMeterFull, (1200, 560))
        if percentage <= 144:
            screen.blit(sets.flagMeterEmpty.subsurface(Rect((0, 0), (157 - percentage, 21))), (1200, 560))
            screen.blit(sets.flagMeterParts1, (1340 - percentage, 560))
        else:
            screen.blit(sets.flagMeterParts1, (1340 - 145, 560))

        screen.blit(sets.flagMeterParts2, (1205, 557))
    # 绘制暂停标志
    def paintPause(self):
        screen.blit(sets.Pause, (500, 0))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 20)
        Str = ft.render("请点击鼠标左键继续", True, (255, 0, 0))
        screen.blit(Str, (562, 92))
    # 绘制开始游戏界面
    def initStartSurface(self):
        screen.blit(sets.surface, (0,0))
        screen.blit(sets.beginBtn, (740,100))
    #绘制游戏失败界面
    def deadPaint(self, screen, sets):
        screen.blit(sets.menuBar, (466, 100))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 45)
        Str = ft.render("游 戏 失 败", True, (255, 255, 255))
        screen.blit(Str, (560, 255))
        # 结束
        screen.blit(sets.selectionBar, (555, 410))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 32)
        Str = ft.render("结  束", True, (60, 60, 60))
        screen.blit(Str, (628, 417))
        # 重新开始
        screen.blit(sets.selectionBar, (555, 340))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 32)
        Str = ft.render("重新开始", True, (60, 60, 60))
        screen.blit(Str, (605, 346))
    #绘制游戏胜利界面
    def wonPaint(self, screen, sets):
        screen.blit(sets.menuBar, (466, 100))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 45)
        Str = ft.render("闯 关 成 功", True, (255, 255, 255))
        screen.blit(Str, (560, 255))
        # 结束
        screen.blit(sets.selectionBar, (555, 410))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 32)
        Str = ft.render("结  束", True, (60, 60, 60))
        screen.blit(Str, (628, 417))
        # 重新开始
        screen.blit(sets.selectionBar, (555, 340))
        pygame.font.init()
        ft = pygame.font.Font('hiw.ttf', 32)
        Str = ft.render("重新开始", True, (60, 60, 60))
        screen.blit(Str, (605, 346))

    # 当鼠标被点击时调用函数
    # 用来绑定卡片监听事件
    def cardMouseClickListener(self):
        leftButtonDown = pygame.mouse.get_pressed()[0]
        rightButtonDown = pygame.mouse.get_pressed()[2]
        if leftButtonDown:
            mousex, mousey = pygame.mouse.get_pos()
            CARD_BASIC_X = 80
            CARD_BASIC_Y = 10
            CARD_HEIGHT = 68
            CARD_WIDTH = 55
            CARD_OFFSET = 60
            # i --> 0-坚果 1-向日葵 2-豌豆射手 3-仙人掌 4-樱桃炸弹 5-豌豆射手double
            # 设置count循环次数 控制暗色植物不能点击
            rangeCount = 0
            if para.sunScore < 50:
                rangeCount = 0
            elif 50 <= para.sunScore < 100:
                rangeCount = 2
            elif 100 <= para.sunScore < 125:
                rangeCount = 3
            elif 150 <= para.sunScore < 200:
                rangeCount = 5
            else:
                rangeCount = 6
            # 选择卡片
            for i in range(rangeCount):
                if CARD_BASIC_X + CARD_OFFSET * i < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * i and \
                        CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
                    dict = {
                        0: para.NUT_SELECTED,
                        1: para.SUNFLOWER_SELECTED,
                        2: para.PEASHOOTER_SELECTED,
                        3: para.CHOMPER_SELECTED,
                        4: para.CHERRY_SELECTED,
                        5: para.REPEATER_SELECTED,
                    }
                    para.cardState = para.CARD_CLICKED
                    para.cardSelection = dict[i]
            ## 选择铲子
            if CARD_BASIC_X + CARD_OFFSET * 6 < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * 6 and \
                    CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
                para.cardState = para.CARD_CLICKED
                para.cardSelection = para.SHOVEL_SELECTED
        if rightButtonDown:
            para.cardState = para.CARD_NOT_CLICKED

    # 用来判断格子的X坐标（即鼠标点击在第几列的格子里）
    def getGridX(self,mouseX):
        if mouseX < sets.gridXIndexes[0]:
            return -1
        for i in range(len(sets.gridXIndexes)):
            if mouseX <= sets.gridXIndexes[i]:
                return i - 1
        return -1

    # 用来绑定卡片监听事件
    def initPlantsMouseClickListener(self):
        leftButtonDown = pygame.mouse.get_pressed()[0]
        if leftButtonDown:
            mouseX, mouseY = pygame.mouse.get_pos()
            gridX = self.getGridX(mouseX)
            gridY = int((mouseY - sets.topY) / sets.gridHeight)
            plantX = sets.gridXIndexes[gridX]
            plantY = sets.topY + sets.gridHeight * gridY
            #鼠标点击在植被上并且未栽种植物
            if mouseX >= sets.leftX and mouseX <= sets.rightX \
                    and mouseY <= sets.bottomY and mouseY >= sets.topY \
                    and para.gridList[gridX][gridY] == -1:
                imagedict = {
                    para.NUT_SELECTED: 0,
                    para.SUNFLOWER_SELECTED: 1,
                    para.PEASHOOTER_SELECTED: 2,
                    para.CHOMPER_SELECTED: 3,
                    para.CHERRY_SELECTED: 4,
                    para.REPEATER_SELECTED: 5,
                }
                plantlist = [
                    Wallnut(screen, plantX, plantY, sets.WallNut),
                    Sunflower(screen, plantX, plantY, sets.SunFlower),
                    Peashooter(screen, plantX, plantY, sets.Peashooter),
                    Cactus(screen, plantX, plantY, sets.Cactus),
                    CherryBomb(screen, plantX, plantY,sets.CherryBomb, self),
                    Repeater(screen, plantX, plantY, sets.Repeater)
                ]
                if para.cardState == para.CARD_CLICKED and para.cardSelection in imagedict:
                    index = imagedict[para.cardSelection]
                    plantlist[index].gridX = gridX
                    plantlist[index].gridY = gridY
                    para.paintPlants.append(plantlist[index])
                    para.cardState = para.CARD_NOT_CLICKED
                    para.sunScore -= plantlist[index].sunshine
                    para.gridList[gridX][gridY] = index
            # 如果选中的是铲子
            elif para.cardState == para.CARD_CLICKED and para.cardSelection == para.SHOVEL_SELECTED \
                    and para.gridList[gridX][gridY] != -1:
                for i in range(len(para.paintPlants)):
                    if para.paintPlants[i].gridX == gridX \
                            and para.paintPlants[i].gridY == gridY:
                        del para.paintPlants[i]
                        break
                para.gridList[gridX][gridY] = -1
                para.cardState = para.CARD_NOT_CLICKED

    def sunMouseClickListener(self):
        # 获取列表  中左键   返回 True  False
        leftFlag = pygame.mouse.get_pressed()[0]
        mouseX, mouseY = pygame.mouse.get_pos()
        # 判断鼠标是否点击到了材料
        for i in range(len(para.sunFall)):
            if leftFlag and para.sunFall[i].x <mouseX < para.sunFall[i].x + para.sunFall[
                i].width and \
                    para.sunFall[i].y < mouseY < para.sunFall[i].y + para.sunFall[i].height:
                para.sunScore += para.sunFall[i].score
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                para.sunFall[i] = Sun(screen, sets.sunImage, xx, yy, goal)
                break
        for i in range(len(para.sunStay)):
            if leftFlag and para.sunStay[i].x < mouseX < para.sunStay[i].x + para.sunStay[
                i].width and \
                    para.sunStay[i].y <mouseY < para.sunStay[i].y + para.sunStay[i].height:
                para.sunScore += para.sunStay[i].score
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                del para.sunStay[i]
                break

    def runOrPause(self):
        leftFlag = pygame.mouse.get_pressed()[0]
        mouseX, mouseY = pygame.mouse.get_pos()
        if 1265 <= mouseX <= 1265 + 113 and 10 <= mouseY <= 10 + 41 and para.state == 1:
            para.state = 2
        elif 740 < mouseX < 740 + 500 and 100 < mouseY < 200 + 100 and para.state == 0:
            para.state = 1
        elif 1257 < mouseX < 1350 and 495 < mouseY < 539:
            sys.exit(0)
        elif leftFlag and para.state == 2:
            para.state = 1
        #重新开始或退出
        elif para.state == 4 or para.state == 3:
            if 555 < mouseX < 780 and 340 < mouseY < 390:
                self.__init__()
                para.state = 0
            elif 555 < mouseX < 780 and 410 < mouseY < 460:
                sys.exit(0)

'''
程序入口
'''
if __name__ == '__main__':
    game=mainGame()
    game.main()

