'''
03-元组
1.元组的语法()
2.元组可以存储各种类型数据
3.元组长度和元素都不可被修改
'''
'''
nameList = ["a","b","c"]
nameList[4] = "d"
print(nameList)
'''
names = ('zhangshan',18,"男",300.0)
#1.查看元素
print(names[0])
#2.增加 --错误
#names[4] = "zhangwuji"
#print(names)
#3.内置函数
print(names.index("zhangshan"))
print(names.count(18))
print(names)
