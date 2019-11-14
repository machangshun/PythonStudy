'''
参数类
'''

class Para():
    # 用于表示是否选择了卡片
    START = 0
    RUNNING = 1
    PAUSE = 2
    END = 3
    DEAD = 4
    #卡片
    CARD_CLICKED = 1  # 鼠标点击上方卡片
    CARD_NOT_CLICKED = 2  # 鼠标未点击上方卡片
    NUT_SELECTED = 3  # 选择了坚果卡片
    CHERRY_SELECTED = 4  # 选择了樱桃卡片
    CHOMPER_SELECTED = 5
    PEASHOOTER_SELECTED = 6  # 选择了豌豆射手卡片
    SUNFLOWER_SELECTED = 7  # 选择了太阳花卡片
    REPEATER_SELECTED = 8  # 选择了豌豆射手double卡片
    SHOVEL_SELECTED = 9  # 选择了铲子卡片
    cardState = 2
    # 表示选择卡片的类型
    cardSelection = 3
    # 表示当前需要绘制的图片
    paintPlants = []
    # 僵尸存储列表
    zombies = []
    # 僵尸频率值
    zombieIndex = 0
    # 掉头信号
    headFlag = True
    zombieRate = 0
    # 存放正在下落太阳的列表
    sunFall = []
    # 存放已经停止的太阳的列表
    sunStay = []
    # 记录初始阳光数的
    sunScore = 100000
    # 全局统一的时间轴
    globalTime = 0
    # 格子的二维数组
    gridList = [([-1] * 5) for i in range(9)]
    # 游戏状态
    state = START
    # 子弹存储列表
    bullets = []
    # 植物频率值
    plantIndex = 0
    # 子弹生成频率值
    shootIndex = 0
    # 游戏结束信号
    endFlag = 0