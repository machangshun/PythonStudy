'''
08-公共方法
+   合并 字符串 列表 元组
* 复制    字符串 列表 元组
in 存在 字符串 列表 元组 字典
not in 不存在 字符串 列表 元组 字典
'''
str1 = "zhangshanfen"
str2 = "wangerma"
str3 = str1 + str2
print(str3)
#字符串的长度不可改变
print(id(str1))
print(id(str2))
print(id(str3))

list1 = ["张学友","张曼玉"]
list2 = ["张国荣","张学良"]
print(list1+list2)

tuple1 = ("zhang",18)
tuple2 = ("z",11)
print(tuple1+tuple2)
print(["我好帅"]*10)


