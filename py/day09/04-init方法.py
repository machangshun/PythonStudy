'''
05-init方法
'''
'''
1.init方法 默认所有的类都有
2.init方法 初始化的自动调用 初始化函数
3.init方法 参数列表默认有一个self
    若要传入参数 则必须在self后添加形参 初始化时需要使用实参进行传递
'''
class Meng(object):
    def __init__(self,name):
        print("wocao",name)
    def run(self):
        print("xiaoma")
#创建对象
meng = Meng("xiao")
meng.run()
