def isrunnian(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
def main():
    num = input("请输入，例如20190316：")
    if isrunnian(int(num[0:4])):
        #是闰年
        j = 0
        for i in range(int(num[4:6])-1):
            j += runnian[i]
        j += int(num[6:])
        print("%s是这年的第%d天" % (num,j))
    else:
        j = 0
        for i in range(int(num[4:6]) - 1):
            j += pingnian[i]
        j += int(num[6:])
        print("%s是这年的第%d天"%(num,j))
if __name__ == '__main__':
    runnian = [31,29,31,30,31,30,31,31,30,31,30,31]
    pingnian = [31,28,31,30,31,30,31,31,30,31,30,31]
 #   print(isrunnian(2019))
    main()