'''
03-类和对象
'''
'''
1.类：看不见摸不着的抽象物体叫类
2.对象：具体的事物 现实中存在的 对象 
3.类和对象的关系？
    类是抽象的 对象是具体的
    四大特征（抽象 继承 多态 封装）
    抽象：将具体事物抽象成数据的形式处理
    继承：提高编码效率 设置共同属性和共同函数
    多态：函数相同 运行的结果不一样
    封装：函数和数据 数据封装在对象中 提高数据的安全性
    
4.类的构成
    类名 类属性（特征） 类方法（函数）
5.类的抽象 将相同属性和相同方法抽象在类中
'''
class Meng(object):
    def __init__(self):
        self.height = 170
        self.age = 18
        self.weight = 100
        self.sex = "女"
    def df(self):
        print("土豆牛肉盖浇饭")
#对象 (女朋友) 初始化类 得到对象 meng
meng = Meng()
print("我的年龄",meng.age)
meng.df()

class cup(object):
    def __init__(self):
        self.height = 100
        self.size = 200
    def drink(self):
        print("i want drink!")
