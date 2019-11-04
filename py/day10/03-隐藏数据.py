'''
03-隐藏数据
'''
class Meng(object):
    def __init__(self):
        self.age = 18
        self.name = "meng"
    def updateName(self,name):
        self.name = "wife"
#对象
m = Meng()
#1.通过属性修改变量值
m.age = 20
#2.通过函数修改变量值
m.updateName("wife")
print(m.age)
print(m.name)

'''
隐藏数据
1.直接通过属性修改值容易参数错误情况
2.不建议使用属性方式进行修改
3.建议使用函数进行变量修改而且是一次性
'''