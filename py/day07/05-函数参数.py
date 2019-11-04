'''
05-函数参数
'''
'''
1.缺省值参数：形参中设置默认值 若实参不传递值，则使用默认值
注意事项：缺省值必须在参数列表最后

'''
#缺省值参数
def add(a,b = 10):
    print("缺省值参数：",a+b)

add(30)
add(10,20)

'''
2.不定长参数
2.1语法规则：*args ===>本质是元组 **kwargs ===>字典
    *args:除了正常形参外 可以接受n个参数值
    **kwargs:参数列表中 设置 = 获取key和value
    
'''
def sum(a,b,*args,**kwargs):
    print("a",a)
    print("b",b)
    print("*args",args)
    print("**kwargs",kwargs)

sum(1,2,3,4,5,m=7,n=7,p=8)

'''
3.引用传参
可变类型 数值可以修改 所以可以调用引用地址进行修改
不可变类型 值不可以修改 所以无法影响 不可变类型的值改变
'''
def delList(names):
    del names[0]
names = ["段正淳","刀白凤","干宝宝","王语嫣"]

delList(names)
print(names)
