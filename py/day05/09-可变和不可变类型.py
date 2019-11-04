'''
可变类型：list dict
不可变类型：int long float bool
str tuple
'''
#不可变量数据不能被改变，一旦改变地址也将改变
bl = True
print(id(True))
b1 = False
print(id(False))
#可变,内容改变，地址不变
name = ["ma","luo"]
print(id(name))
name[1] = "huang"
print(id(name))