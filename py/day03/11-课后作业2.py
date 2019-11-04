print("新龙门客栈系统")
print("="*30)
print("1.大床房   128元")
print("2.标间     138元")
print("3.三人间   158元")
print("4.豪华标间 178元")
print("5.总统套房 888元")
print("6.退出系统")
print("="*30)
choose = int(input("请选择房间："))
if choose ==1:
    house = "大床房"
    price = 128
elif choose == 2:
    house = "标间"
    price = 138
elif choose == 3:
    house = "三人间"
    price = 158
elif choose == 4:
    house = "豪华标间"
    price = 178
elif choose == 5:
    house = "总统套房"
    price = 888
else:
    quit(0)
print("="*30)
print("1.微信支付")
print("2.支付宝")
print("3.现金")
print("4.刷卡")
print("5.支票")
print("6.刷脸")
print("="*30)

chos = int(input("请选择支付方式："))
if chos == 1:
    pay = "微信支付"
elif chos == 2:
    pay = "支付宝"
elif chos == 3:
    pay = "现金"
elif chos == 4:
    pay = "刷卡"
elif chos == 5:
    pay = "支票"
elif chos == 6:
    pay = "刷脸"

name = input("请输入您的姓名：")
id_ = input("请输入您的身份证：")
while len(id_) != 18:
    print("身份证号码输入错误！请重新输入：")
    id_ = input("请输入您的身份证：")
phone = input("请输入您的联系方式：")
while len(phone) != 11:
    print("电话号码输入错误！请重新输入：")
    phone = input("请输入您的联系方式：")
print("您的入住信息：")
print("%s   %s  %s  欢迎入住%s %s%d元"%(name,id_,phone,house,pay,price))