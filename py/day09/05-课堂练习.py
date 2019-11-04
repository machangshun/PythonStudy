'''
课堂练习：
准备工作
1.新建文件 yuwen.txt yingyy.txt shuxue.txt
 info.txt
 存储10个人的成绩
 name:张三，studentId：。。，score：90
 。。。。
 info.txt
 name:zhanshan,studentid:..pwd:...
 2.新建类 studentInfo
    类属性：name,studentId,pwd,score
    类方法：selectYuWen
            selectYingYu
            selectShuXue
            login
3.用户输入id和密码进行比较登陆
4.根据所输入的id进行查找该学生三科成绩
'''
'''
file1 = open("yuwen.txt","w",encoding="utf-8")
file2 = open("yingyu.txt","w",encoding="utf-8")
file3 = open("shuxue.txt","w",encoding="utf-8")
file4 = open("info.txt","w",encoding="utf-8")
for i in range(0,10):
    context = "name:"+"%d,"%i+"studentId:"+"%d,"%i+"score:"+"%d\n"%(90+i)
    file1.write(context)
for i in range(0,10):
    context = "name:"+"%d,"%i+"studentId:"+"%d,"%i+"score:"+"%d\n"%(89+i)
    file2.write(context)
for i in range(0,10):
    context = "name:"+"%d,"%i+"studentId:"+"%d,"%i+"score:"+"%d\n"%(91+i)
    file3.write(context)
for i in range(0,10):
    context = "name:"+"%d,"%i+"studentId:"+"%d,"%i+"pwd:"+"%d\n"%(90+i)
    file4.write(context)
'''
class StudentInfo(object):
    def __init__(self):
        self.name = ""
        self.student = ""
        self.pwd = ""
        self.score = ""
        self.yuwenList = []
        self.yingyuList = []
        self.shuxueList = []
    def loadDB(self):
        f = open("yuwen.txt","r")
        context = f.readlines()
        for line in context:
            lineList = line.split(",")
            dict = {}
            for db in lineList:
                dbList = db.split(":")
                keyStr = str(dbList[0])
                dict[dbList[0]] = dbList[1]
                self.yuwenList.append(dict)
    def selectYuWen(self,studentId):
        for dict in self.yuwenList:
            if dict["studentId"] == studentId:
                return dict["score"]
    def selectYingYu(self):
        pass
    def selectShuXue(self):
        pass
    def login(self,name,studentId,pwd):
        file = open("info.txt","r")
        context = file.readlines()
        for text in context:
            Name = text[5:text.find(",")]
            StudentId = text[text.find("Id:")+3:text.find(",pwd")]
            Pwd = text[text.rfind(":")+1:-1]
            if Name == name and StudentId == studentId and Pwd == pwd:
                print("登陆成功！")
                return True
        file.close()

if __name__ == '__main__':
    stu = StudentInfo()
    name = input("name")
    studentId = input("studentId")
    pwd = input("pwd")
    stu.loadDB()
    score = stu.selectYuWen(studentId)
    print(score)
    if stu.login(input("name:"),input("studentId:"),input("pwd")):
        stu.selectYuWen()



