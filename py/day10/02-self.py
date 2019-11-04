'''
02-self
'''
'''
self:
1.self:是指代当前对象 存储的是当前对象的引用地址
2.当对象生成时，python解释器会自动将自己的引用地址作为参数传递个init函数的第一形参
'''
class Meng(object):
    def __init__(self):
        print("init函数：",id(self))

meng = Meng()
print(id(meng))
m2 = Meng()
print(id(m2))