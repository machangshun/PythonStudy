'''
100,50,20,5,1的面额
找376元 用最少的数量
'''
#t表示所有商店的零钱面额
t = [100,50,20,5,1]
#n表示n元钱
def change(t,n):
    w = [0 for _ in range(len(t))]
    for i,money in enumerate(t):
        print(i,money)
        w[i] = n // money
        n = n % money
    return w,n

print(change(t,376))