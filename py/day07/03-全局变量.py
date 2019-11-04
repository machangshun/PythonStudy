'''
03-全局变量
'''
'''
全局变量
1.定义：类对象中 所有函数都可以使用的变量
2.全局变量和局部变量名字相同 局部变量使用在局部 其他都是全局变量
    是否是同一个变量? 不是
3.修改全局变量
    3.1语法规则 global 声明为全局变量
    3.2全局变量不可改变（函数/方法区中） 引用地址
    重新定义一个变量 
    在进行运算修改处理   
    将结果保存在重新的变量上
    将引用地址覆盖
2.可变类型
    list dict
  不可变类型
'''
#全局变量和局部名字相同
ap = 500
def add():
    ap = 300
    print("函数内：",ap)
    print(id(ap))
add()
print("函数外：",id(ap))

#修改全局变量
ag = 200
print("ag函数前：",id(ag))
def sum():
    global ag
    ag += 300
    print("ag函数内：",id(ag))
    print("ag函数内：",ag)
sum()
print("ag函数后：",id(ag))

#可变类型全局变量
names = ["杨过","小龙女","公孙绿颚"]
print("names:",id(names))
print("小龙女",id(names[1]))
def delList():
    del names[0]
    print("names:",id(names))
    print("小龙女")
delList()
print(names)

name = "郭襄"
def updateName():
    name = "陆无双"
    print("修改函数：",name)
updateName()
print(name)