'''
05-函数的类型
'''
'''
函数类型
1.无参无返回值
2.无参有返回值
3.有参无返回值
4.有参有返回值

main函数：程序主入口
拥有main函数的.py文件就必须从main函数调用其他函数
'''
#1
def function():
    pass
#2
def function2():
    return "handsome"
#3
def function3(money):
    pass
#4
def function4(money):
    return "handsome"
if __name__ == '__main__':
    #自动调用该函数
    function()

