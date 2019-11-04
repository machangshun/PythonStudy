'''
04-函数的返回值
'''
'''
函数的返回值
1.语法规则：return
2.返回值类型：基本数据类型、字符串、字典、列表、元组、对象都可以
3.返回数量：返回多个变量 注意事项：返回类型为tuple(元组)
'''
def df(money):
    if money > 20:
        return "土豆牛肉盖浇饭"
    elif   money > 15:
        return "土豆肉丝盖浇饭"
    elif money >10:
        return "青椒土豆丝盖浇饭"
print("我要吃%s啦"%df(30))
def df2():
    return "ma","chang"
name = df2()
print(name)
print(type(name))
