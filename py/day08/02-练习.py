'''
02-复制文件

'''
oldFile = input()
file = open(oldFile,"r")
if file:
    filePoint = oldFile.rfind(".")
    fileName = oldFile[:filePoint]
    fileLater = oldFile[filePoint:]
    newFileName = fileName+"[复件]"+fileLater
    context = file.read()
    newFile = open(newFileName,"w")
#   context = file.readlines()
#    for line in context:
#        newFile.write(line)
    newFile.write(context)
    file.close()
    newFile.close()