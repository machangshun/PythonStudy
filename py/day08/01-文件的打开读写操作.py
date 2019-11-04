'''
1.文件打开
    open(文件名，模式)
2.文件关闭filename.close()
模式：
1.r 文件读，指针默认在文件开头
2.w 文件写，指针默认在开头 若有文件，则打开时写入覆盖原文件内容 若没有则新建文件并写入
3.a 文件追加，指针在文件末尾 在文本后追加内容 没有文件时会新建该文件
4.rb 二进制的形式
5.wb
6.ab
7.r+ 打开文件进行读写 指针在文件开头
8.w+ 打开文件进行读写 如果文件已存在则将其覆盖
9.a+ 打开文件进行读写
'''
'''
写操作filename.write("")
读操作filename.read() 全部内容
    filename.readline() 单行读取(指针所在位置后)
    filename.readlines() 多行读取 返回的类型是列表 文中自带\n
'''
f = open("test.txt","w")
f.write("Hello World!!\nHow are you?\nl'm file,thank you,and you?")
f = open("test[复件].txt","r")
context = f.readlines()
print(context)
f.close()