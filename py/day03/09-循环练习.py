"""
1.猜数字 使用循环知道猜中为止
2.使用for循环 99乘法表
"""
import random
randNum = random.randint(0,100)
userNum = int(input("please input number:"))
#userNum = random.randint(0,100)
while randNum != userNum:
    if randNum > userNum>=0:
        print("猜小了")
    elif randNum < userNum<=100:
        print("猜大了")
    userNum = int(input("please input number:"))
#    userNum = random.randint(0, 100)
print("猜中了")