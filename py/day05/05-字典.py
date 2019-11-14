'''
05-字典
1.字典语法 {}
2.键值对 key:value
3.key唯一性    value可以重复
4.访问字典 根据KEY 进行访问
'''
names = {"name":"张三丰","age":18,"sex":"男"}
names["name"] = "张无忌"
print(names)

#添加元素
names["salary"] = 30000
print(names)
#删除元素del clear
del names["name"]
print(names)

names.clear()
print(names)


