'''
课堂练习：
1.批量修改文件名：
    1.1新建文件夹 马哥出品
    1.2新建10个文件 ===》所有文件在马哥出品
        Hello01.txt
        ...
        Hello10.txt
    1.3批量修改文件名
    Hello01.txt ==>Hello-[马哥出品]-01.txt
    Hello-[..]-10.txt
'''
import os
os.mkdir("马哥出品")
os.chdir("马哥出品")

for i in range(1,11):
    filename = "Hello"+"%02d"%i+".txt"
    f = open(filename,"w")
    f.write("Hello!")
    f.close()
'''
for i in range(1,11):
    filename = "Hello"+"%02d"%i+".txt"
    refilename = filename[:5]+"-[马哥出品]-"+"%02d"%i+".txt"
    os.rename(filename,refilename)
    f.close()
'''
fileList = os.listdir("./")
print(fileList)
#del fileList[len(fileList)-1]
for fileName in fileList:
    #对复制的文件进行解析
    filePoint = fileName.rfind(".")
    fileFront = fileName[:5]
    fileNum = fileName[5:filePoint]
    fileLater = fileName[filePoint:]
    newFile = fileFront + "-[马哥出品]-"+fileNum+fileLater
    os.rename(fileName,newFile)
