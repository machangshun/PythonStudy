'''
魔法方法：
1.类对象会自动调用该函数 __init__
2.类对象会根据场景调用
'''
class Car(object):
    def __init__(self,newwheelNum,newColor):
        self.wheelNum = newwheelNum
        self.colo = newColor
#自动调用字符串的方法
    def __str__(self):
        msg = ("我有一辆%d驱车，颜色是%s"%(self.wheelNum,self.colo))
        return msg
    def move(self):
        print("my car run")

#生成对象
bmw = Car(4,"白色")
print(bmw)