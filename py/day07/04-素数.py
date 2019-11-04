def judueNum(i):
    for b in range(2,int(i**0.5)+1):
        if i % b == 0:
            return False
        else:
            return True

if __name__ == '__main__':
    for i in range(100,201):
        if judueNum(i):
            print(i,end = " ")