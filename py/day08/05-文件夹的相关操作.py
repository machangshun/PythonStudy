'''
05-文件夹的相关操作
'''
import os
#1.创建文件夹 mkdir()
os.mkdir("马哥出品")
#2.获取当前目录 getcwd()
#绝对路径 相对路径
print("当前目录：",os.getcwd())

#3.改变目录 chdir()
os.chdir("../")
print("改变目录：",os.getcwd())

#4.获取目录列表 listdir()函数
#修改目录
os.chdir("day08")
print("目录列表：",os.getcwd())

fileList = os.listdir("./")
print("目录列表：",fileList)

#5.删除文件夹 rmdir()
os.rmdir("马哥出品")
