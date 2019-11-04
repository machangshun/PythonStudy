'''
07-if
'''
house = 1000000
car = 100000
salary = 20000
money = 100000
if house >= 1000000:
    print("我们试试看吧！")
    if car >= 100000:
        print("你现在有女盆友了！")
        if salary >= 20000:
            print("亲爱的，啥时见爸妈！")
        else:
            print("我还有事！")
    else:
        print("你是个好人！")
else:
    print("我喜欢头方的")
# 年龄大于18岁
#money >= 30000 越南走一趟
age = 18
if age >= 18:
    print("欢迎光临！")
#else:
#   print("拒入！")
elif age <= 0:
    print("拒入！")
