i = 1
j = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d"%(j,i,i*j),end = "      ")
        j += 1
    i += 1
    print("\n")
#while循环注意事项
#1.while循环判断 尽量不要使用while True
#2.尽量不要嵌套超三层