'''
图片处理类
'''
import os,pygame
from pygame.locals import *
class setImage(object):
    def __init__(self):
        pygame.display.init()
        self.background = pygame.image.load('image/background1.jpg')
        self.seedBank = pygame.image.load('image/SeedBank.png')
        self.sunImage = pygame.image.load('image/sun.png')
        # 进度条   指示标   终点标
        self.flagMeterEmpty = pygame.image.load('image/progress_bar/FlagMeterEmpty.png')
        self.flagMeterFull = pygame.image.load('image/progress_bar/FlagMeterFull.png')
        self.flagMeterParts1 = pygame.image.load('image/progress_bar/FlagMeterParts1.png')
        self.flagMeterParts2 = pygame.image.load('image/progress_bar/FlagMeterParts2.png')
        # 提示标语
        self.prepareGrowPlants = pygame.image.load('image/prompt_words/PrepareGrowPlants.png')
        self.largeWave = pygame.image.load('image/prompt_words/LargeWave.png')
        self.finalWave = pygame.image.load('image/prompt_words/FinalWave.png')
        # 游戏状态
        self.Button = pygame.image.load('image/game_state/Button.png')
        self.Pause = pygame.image.load('image/game_state/Pause.png')

        # 普通僵尸
        self.zombie_normalImages = self.getImage("image/zombie_normal/")
        # 帽子僵尸
        self.zombie_coneheadImages = self.getImage("image/zombie_conehead/")
        # 铁桶僵尸
        self.zombie_bucketImages = self.getImage("image/zombie_bucket/")

        # 掉头僵尸
        self.zombieLostHeadImages = self.getImage("image/zombieLostHead/")
        # 掉头
        self.zombieHeadImages = self.getImage("image/zombieHead/")
        # 普通僵尸碰撞图片
        self.normalAttackImages = self.getImage("image/zombie_normalAttack/")

        # 帽子僵尸碰撞图片
        self.coneheadAttackImages = self.getImage("image/zombie_coneheadAttack/")
        # 铁桶僵尸碰撞图片
        self.bucketAttackImages = self.getImage("image/zombie_bucketAttack/")

        # 僵尸死掉
        self.zombieDieImages =self.getImage("image/zombieDie/")

        # 掉头僵尸碰撞图片
        self.zombieLostHeadAttackImages = self.getImage("image/zombieLostHeadAttack/")
        self.zombie_charred = [
            pygame.image.load("image/zombie_dead/Zombie_charred1.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred2.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred3.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred4.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred5.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred6.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred7.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred8.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred9.png"),
            pygame.image.load("image/zombie_dead/Zombie_charred10.png"),
        ]
        self.Cactus = self.getImage("image/plants/Cactus/")
        self.CherryBomb = self.getImage("image/plants/CherryBomb/")
        self.CherryBombBoom = self.getImage("image/plants/CherryBombBoom/")
        self.WallNut = self.getImage("image/plants/WallNut/")
        self.Peashooter = self.getImage("image/plants/Peashooter/")
        self.Repeater = self.getImage("image/plants/Repeater/")
        self.SunFlower = self.getImage("image/plants/SunFlower/")
        self.WallNutBadlyCracked = self.getImage("image/plants/WallNutBadlyCracked/")
        self.WallNutCracked = self.getImage("image/plants/WallNutCracked/")
        # 加载卡片路径
        self.cardNutWall = pygame.image.load('image/card/nutWall.png')
        self.cardPeashooter = pygame.image.load('image/card/peashooter.png')
        self.cherry = pygame.image.load('image/card/cherry.png')
        self.cactus = pygame.image.load('image/card/cactus.png')
        self.sunflower = pygame.image.load('image/card/sunflower.png')
        self.cardPeashooterdouble = pygame.image.load('image/card/peashooterdouble.png')
        self.cardShovelBack = pygame.image.load('image/card/ShovelBack.png')
        self.cardShovel = pygame.image.load('image/card/Shovel.png')
        self.cardNutWallDark = pygame.image.load('image/card/nutdark.png')
        self.cardPeashooterDark = pygame.image.load('image/card/peashooterdark.png')
        self.cherryDark = pygame.image.load('image/card/cherrydark.png')
        self.cactusDark = pygame.image.load('image/card/cactusdark.png')
        self.sunflowerDark = pygame.image.load('image/card/sunflowerdark.png')
        self.cardPeashooterdoubleDark = pygame.image.load('image/card/peashooterdoubledark.png')
        # 卡片图片缩放
        self.cardNutWall = pygame.transform.scale(self.cardNutWall, (55,68))
        self.cardPeashooter = pygame.transform.scale(self.cardPeashooter, (55, 68))
        self.cherry = pygame.transform.scale(self.cherry, (55, 68))
        self.cactus = pygame.transform.scale(self.cactus, (55, 68))
        self.sunflower = pygame.transform.scale(self.sunflower, (55, 68))
        self.cardPeashooterdouble = pygame.transform.scale(self.cardPeashooterdouble, (55, 68))
        self.cardShovelBack = pygame.transform.scale(self.cardShovelBack, (70,86))
        self.cardShovel = pygame.transform.scale(self.cardShovel, (55,55))
        self.cardNutWallDark = pygame.transform.scale(self.cardNutWallDark, (55, 68))
        self.cardPeashooterDark = pygame.transform.scale(self.cardPeashooterDark, (55, 68))
        self.cherryDark = pygame.transform.scale(self.cherryDark, (55, 68))
        self.cactusDark = pygame.transform.scale(self.cactusDark, (55, 68))
        self.sunflowerDark = pygame.transform.scale(self.sunflowerDark, (55, 68))
        self.cardPeashooterdoubleDark = pygame.transform.scale(self.cardPeashooterdoubleDark, (55, 68))
        #图片旋转
        self.cardShovel = pygame.transform.rotate(self.cardShovel, 45)
        # 卡片点击图片集合
        self.cardImgs = [
            pygame.image.load('image/mouseMoveCard/mouseNut.gif'),
            pygame.image.load('image/mouseMoveCard/mouseSunflower.gif'),
            pygame.image.load('image/mouseMoveCard/mousepeashooter.gif'),
            pygame.image.load('image/mouseMoveCard/mouseCactus.png'),
            pygame.image.load('image/mouseMoveCard/mouseCherry.gif'),
            pygame.image.load('image/mouseMoveCard/repeater.gif'),
            self.cardShovel
        ]
        # 豌豆、仙人掌子弹贴图
        self.peaBulletImg = pygame.image.load('image/peaBullet.png')
        self.cactusBulletImg = pygame.image.load('image/bullet_02.png')
        self.cactusBulletImg= pygame.transform.scale(self.cactusBulletImg, (24, 24))
        # 格子X坐标
        self.gridXIndexes = [260, 340, 418, 500, 583, 662, 740, 820, 910, 996]
        # 格子高度：
        self.gridHeight = 95
        # 下边界
        self.bottomY = 574
        # 左边界：
        self.leftX = self.gridXIndexes[0]
        # 上边界：
        self.topY = self.bottomY - 5 * self.gridHeight
        # 右边界：
        self.rightX = self.gridXIndexes[9]
        # 开始界面图片加载
        self.surface = pygame.image.load('image/Surface.jpg')
        self.surface = pygame.transform.scale(self.surface, (1400,600))
        self.beginBtn = pygame.image.load('image/beginBtn.png').subsurface(Rect((0, 0), (329, 148)))
        self.beginBtn = pygame.transform.scale(self.beginBtn, (500,200))
        #结束界面图片加载
        self.zombiewin = pygame.image.load('image/ZombiesWon.png')
        self.selection = pygame.image.load('image/selection.png')
        self.banner = pygame.image.load('image/banner.png')
        self.menuBar = pygame.image.load('image/menuBar.png')
        self.selectionBar = pygame.image.load('image/game_state/Button.png')
        self.selectionBar = pygame.transform.scale(self.selectionBar, (230, 50))

    def getImage(self,dir):
        # 统计图片的数量
        imageCounts = 0
        for i in os.listdir(dir):
            imageCounts += 1
        images = []
        for j in range(imageCounts):
            imageStr = dir + str(j) + '.png'
            img = pygame.image.load(imageStr)
            images.append(img)
        return images
