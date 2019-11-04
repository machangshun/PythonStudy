'''
01.if练习
'''
'''
'''
grade = int(input("please input grade:"))
if 90 <= grade <= 100:
    print("优秀")
elif 80<= grade < 90:
    print("良好")
elif 70<= grade < 80:
    print("中等")
elif 60<= grade < 70:
    print("及格")
elif grade <60:
    print("不及格")
else:
    print("请重新输入！")