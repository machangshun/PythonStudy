'''
07-匿名函数
1.定义：没有函数名的函数
2.语法规则：lambda 匿名函数
'''
#函数名 形参 代码块
sum = lambda a,b:a+b
def sum1():
    return a+b
print("加法运算：",sum(10,20))

'''
函数作为参数传递
'''
def add(a,b,opt):
    print("a:",a)
    print("b:",b)
    print("opt:",opt(a,b))
add(10,20,lambda x,y:x+y)

'''
内置函数
'''
stus = [{"name":"zhangshan","age":18},{"name":"lisi","age":19},{"name":"wangwu","age":30}]
stus.sort(key = lambda x:x["name"])
print(stus)