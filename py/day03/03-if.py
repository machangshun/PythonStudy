import random
randNum = random.randint(0,10)
userNum = int(input("please input your number:"))
if randNum == userNum:
    print("猜中了")
elif randNum > userNum:
    print("猜小了")
elif randNum < userNum:
    print("猜大了")
else:
    print("输入错误，请重新输入！")