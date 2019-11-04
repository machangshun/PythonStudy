'''
07-判断闰年
'''
def isrunnian(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Yes!")
    else:
        print("Not!")
isrunnian(int(input("输入年份")))