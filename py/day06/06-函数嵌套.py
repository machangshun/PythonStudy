'''
06-函数嵌套
'''
def A():
    print("A函数前")
    B()
    print("A函数后")
def B():
    print("B函数中")
A()