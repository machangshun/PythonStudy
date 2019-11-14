'''
01-字符串
""或''
字符串拼接或html里面内容读写"  ' '  "
一般是函数区中存储 堆和栈 预编译操作 字符串长度一般不可变
id() 查找变量的引用地址 栈中存地址 堆中存内容
'''
name = "zhangshan"
name2 = 'zhansan'
print(type(name))
print(type(name2))

print("id地址：",id(name))
name = "wang"
print("改后：",id(name))
