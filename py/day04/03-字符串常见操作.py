address = "南京市江宁区禄口街道航金大道88号"
#1.find()，返回下标，没有返回-1
print("find函数：",address.find("区"))
print("find函数",address.find("省"))
#2.index()查找 找到返回下标，没有就报错
print("index函数：",address.index("区"))
#print("index函数：",address.index("省"))

#3.replace() 替换 找到替换
print("replace函数：",address.replace("88","99"))
print("replace函数：",address.replace("77","66"))

#4.count()统计
#统计到 返回数量
#统计不到 返回0
print("count函数：",address.count("口"))
print("count函数：",address.count("嘴"))

#5.split 分隔
print("split()函数：",address.split("口"))

#6.字符串首字母大写capitalize
hello = "hello world"
print(" 函数：",hello.capitalize())
#7.每个单词首字母大写
print("title()",hello.title())

#8.startswith 以obj为开头
#是开头则返回True
print("startswith函数：",address.startswith("南京市"))

#9.endswith 以obj结尾.lower转换为小写
print("endswith函数：",address.endswith("88号"))

#10
hello = "HELLOWORLD"
print("lower函数：",hello.lower())

#11.upper转换为大写
hello = "helloworld"
print("upper函数：",hello.upper())

#12.ljust 返回一个字符串左对齐 空格填充
hello = "hello"
print("ljust函数：",hello.ljust(15),end = "?")
print("")
#13.rjust
print("rjust函数：",hello.rjust(15))

#14.center 返回一个字符串 居中 两边空格填充
print("center函数：",hello.center(20),end = "|")
print("")
#15.lstrip 删除左边空白
hello = "           world"
print("lstrip删除左边空白：",hello.lstrip())
#16.rstrip 删除右边空白
hello = "world          "
print("rstrip():",hello.rstrip())
#17.strip 删除两边空白
hello = "       hel lo       "
print("strip():",hello.strip(),end = "?")
print("")

#18.rfind 右边查找
ress = "江宁区禄口区"
print("rfind():",ress.rfind("区"))
#19.rindex 右边查找
print("rindex():",ress.rindex("区"))
#20.partition 分割成三个部分 元组
print("partition():",address.partition("禄口街道"))

#21.rpartition 右边进行分割
ress = "江宁区玄武区栖霞区"
print("rpartition():",ress.rpartition("区"))

#22.splitlines 按行分割成元素列表
hello = "hello\nworld"
print("splitlines():",hello.splitlines())

#23.isalpha 判断是否全是字母 返回True和false
hello = "helloworld"
print("isalpha():",hello.isalpha())

#24.isalnum 判断是否是数字或字母
num = "num12"
print("isalnum():",num.isalnum())

#25.isdigit 判断是否字符串是否为数字
nums = "123"
print("isdigit():",nums.isdigit())

#26.isspace 判断是否全是空格
nums = "  "
print("isspace():",nums.isspace())
#27.join 每个字符后插入一个新的字符串
str = "#"
lists = ["my","name","mac"]
print("join():",str.join(lists))
s = "#"
stu = "student"
print(s.join(stu))
