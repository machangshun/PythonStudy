'''
2.2花千骨
    2.1 gu.txt
    2.2 统计gu.txt 中的花千骨 总共出现的次数
    将花千骨所在位置的 指针记录下来
    将统计的数据 存储到 guCount.txt中
    [
    {"花":22,}
    ]
'''
f = open("gu.txt",encoding='utf-8')
file = open("guCount.txt","w",encoding="utf-8")
context = f.read()
num = context.count("花千骨")
print("出现次数：",num)
#print("花千骨：",t,context.count("花千骨"),f.tell())
flag = 0
q = 0
for i in context:
    if i == "花":
        flag += 1
        continue
    if flag == 1 and i == "千":
        flag += 1
        continue
    if flag == 2 and i == "骨":
        q += 2
        text = "花"+"%d"%(q-2)+"千"+"%d"%(q-1) + "骨"+"%d"%q
        print(text)
        file.write(text+"\n")
        continue
    q += 1
    flag = 0
#    print(i,end = "")
f.close()
file.close()