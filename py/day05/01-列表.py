'''
01-列表
列表语法【'',''】
'''
nameList = ['macs','ljy','hm','yhl']
#1.输出打印
print(nameList[0])
#2.列表的循环遍历
for name in nameList:
    print(name)
i = 0
while i < len(nameList):
    print(nameList[i])
    i += 1
#3.列表的常见操作
#3.1增加元素    append insert extend
#append添加元素 在列表的最后添加元素
nameList.append("kmp")
print(nameList)
#insert插入元素
nameList.insert(1,"huo")
print(nameList)
#extend 添加元素
nameList.extend(["a","b","c"])
print(nameList)

#3.2 删除 del pop remove
#下标
del nameList[1]
print(nameList)
#删除最后一个元素
nameList.pop()
print("pop:",nameList)

#remove 元素值
nameList.remove("b")
print(nameList)

#删除列表 del 切片
del nameList[:]
print(nameList)

#3.3改元素 根据下标修改
names = ["乔峰","虚竹","段誉"]
names[2] = "段正淳"
#names["虚竹"] = " "
print(names)

#3.4 查找元素 index,count,in ,not in
#index 查找元素 返回元素下标
print(names.index("乔峰"))
#count
print(names.count("虚竹"))
#in 如存在返回True 若不在返回False
print("虚竹"in names)
#not in 若存在返回False 。。。
print("虚竹" not in names)
#反转
names.reverse()
print(names)
names.clear()
print(names)