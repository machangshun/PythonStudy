'''
02-下标和切片
'''
address = "machangshun"
print(len(address)-1)
print(address[3])
'''
切片
语法：【起始：结束：步长】
1.起始位置不写，默认为0
2.末端位置不写，默认为到最后一位
3.步长不写，则为加1
4.加符号，取相反位置
'''
#1.macs
print(address[0:3])
print(address[0:])
print(address[:])
#隔一个取
print(address[0::2])
#隔一个取
print(address[1::2])

print(address[-1:])

print(address[9::-1])