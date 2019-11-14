f = open("gu.txt","r",encoding="utf-8")
countstr = f.read()
countIndex = countstr.count("花千骨")
#for line in context:
#    countIndex += line.count("花千骨")

print("花千骨：%d"%countIndex)
'''
统计指针位置
'''
#设置空字符串
#countstr = ""
#for line in context:
#    countstr += line
#查找花千骨
#index = countstr.find("花千骨")
#替换 replace(老字符串，新字符串) 替换所有的字符

#遍历查询
countList = []
for index in range(0,countIndex):
    ix = countstr.find("花千骨")

    countList.append(ix)
    #切片 ix花
    countstr = countstr[ix+3:]
#列表处理
for index in range(1,len(countList)):
    countList[index] += countList[index-1]
print(countList)

#写入文本
file = open("gucount.txt","w",encoding="utf-8")
for index in countList:
    file.write("花：%d，千：%d,骨：%d\n"%(index,index+1,index+2))


f.close()
file.close()
