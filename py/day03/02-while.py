flag = 1
grade = int(input("please input grade:"))
while flag == 1:
    if 90 <= grade <= 100:
        flag = 0
        print("优秀")
    elif 80 <= grade < 90:
        flag = 0
        print("良好")
    elif 70 <= grade < 80:
        flag = 0
        print("中等")
    elif 60 <= grade < 70:
        flag = 0
        print("及格")
    elif 0 <= grade < 60:
        flag = 0
        print("不及格")
    else:
        flag = 1
        print("请重新输入！")
        grade = int(input("please input grade:"))
