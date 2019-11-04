'''
列表
infoList = [
    {"name":"mac","id":"2016023122","pwd":123,"sex":"男"}
]
yuwenList = [
    {"id":....,"name":"mac","grade":70}
]
englishList = [

]
shuxueList = [

]
1.登陆系统
2.查询出各科成绩
'''

infoList = [
    {"name":"mac","id":"2016023122","pwd":"123","sex":"男"},
    {"name":"hm","id":"2016023123","pwd":"12345","sex":"男"},
]
yuwenList = [
    {"id":"2016023122","name":"mac","grade":70},
    {"id":"2016023123","name":"hm","grade":80}
]
englishList = [
    {"id":"2016023122","name":"mac","grade":80},
    {"id":"2016023123","name":"hm","grade":80}
]
shuxueList = [
    {"id":"2016023122","name":"mac","grade":100},
    {"id":"2016023123","name":"hm","grade":80}
]
def login():
    name = input("请输入姓名：")
    id_ = input("请输入学号：")
    pwd = input("请输入密码：")
    for stu in infoList:
        if stu["name"] == name and stu["id"] == id_ and stu["pwd"] == pwd:
            print("登陆成功")
            return id_
    else:
        return False
def searchgrade(id_):
    '''
    print("="*30)
    print("1.语文成绩")
    print("2.英语成绩")
    print("3.数学成绩")
    print("="*30)
    i = int(input("请选择您要查询的成绩："))
    '''
    for grade in yuwenList:
        if grade["id"] == id_:
            print("语文", grade["grade"])
    for grade in englishList:
        if grade["id"] == id_:
            print("英语",grade["grade"])
    for grade in shuxueList:
        if grade["id"] == id_:
            print("数学",grade["grade"])

if __name__ == '__main__':
    print("=" * 30)
    print("学生信息管理系统")
    print("=" * 30)
    while True:
        id_ = login()
        if id_:
            searchgrade(id_)
        else:
            print("登陆失败，请重新输入！")

