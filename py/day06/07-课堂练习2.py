'''
1.按姓名查找
2.按下标修改
'''

def insert():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入qq:")
    address = input("请输入地址：")
    idcard.append({"name": name, "phone": phone, "qq": qq, "address": address})
    for card in idcard:
        print(card)
def delete():
    name = input("请输入您要删除名片的姓名：")
    for personal in idcard:
        if personal["name"] == name:
            idcard.remove(personal)
            print("%s的名片已删除！" % name)
            break
    else:
        print("查无此人！")
def modif():
    name = input("请输入您要修改名片的姓名：")
    for personal in idcard:
        if personal["name"] == name:
            personal["name"] = input("请输入姓名：")
            personal["phone"] = input("请输入手机电话：")
            personal["qq"] = input("请输入qq:")
            personal["address"] = input("请输入地址：")
            print("名片已修改！")
            break
    else:
        print("查无此人！")
def search():
    name = input("请输入您要查询的姓名：")
    for personal in idcard:
        if personal["name"] == name:
            for key, value in personal.items():
                print("%s:%s" % (key, str(value)))
            break
    else:
        print("查无此人！")
def choose():
    print(" 名片系统   ")
    print("=" * 30)
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.退出系统")
    print("=" * 30)
    while True:
        i = int(input("请选择操作："))
        if i == 1:
            insert()
        elif i == 2:
            delete()
        elif i == 3:
            modif()
        elif i == 4:
            search()
        elif i == 5:
            break
        else:
            print("请重新选择操作：")

if __name__ in '__main__':
    idcard = []
    people = {}
    choose()