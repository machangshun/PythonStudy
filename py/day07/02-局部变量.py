'''
02-局部变量
'''
'''
局部变量：
1.定义：函数内声明的变量为局部变量
2.定义域：函数内   函数结束    变量消失
3.不同函数可以定义相同变量名，之间不会有影响

'''
#局部变量
def eat():

    fan = "土豆牛肉盖浇饭"

eat()
def drink():
    fan = "珍珠奶茶"
drink()
