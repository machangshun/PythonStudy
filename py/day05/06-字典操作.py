names = {"name":"张半仙","sex":"男","age":18}
#1.len()
names["salary"] = 30000
print("len():",names.__len__())
#2.keys() 查找字典中所有key值
print("key():",names.keys())

#3.values() 函数 查找字典中所有的value值
print("values():",names.values())

#4.items()函数 查找字典中所有的key-value键值对
print("items():",names.items())

#5.has_key() 函数 python2.x版本有效
