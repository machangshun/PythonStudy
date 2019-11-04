#1.获取文件当前位置tell()
f = open("read.txt","rb")
context = f.read(5)
print("指针位置：",context)
print("指针位置：",f.tell())

#2.定位到某个位置 seek(偏移量offset,方向from)
#offset：偏移的量
#from：0开头的位置 1当前位置 2 文件末尾
#注意事项：1.读取的时换行符\n算一个字符
#2.python2.x版本支持f.seek(11,1)
#pythone3.x版本支持方式不同
#！！01 从开头定位置
f.seek(11,0)
context = f.readline()
print("定位位置：",context,f.tell())
f.seek(11,1)
context = f.readline()
print("定位位置：",context,f.tell())

#!!10从文件末尾开始偏移
f.seek(-4,2)
context = f.readline()
print("当前位置：",context,f.tell())

f.close()