'''
06-递归函数
'''
#阶乘
def calNum(num):
    if num >= 1:
        result = num * calNum(num-1)
    else:
        result = 1
    return result
result = calNum(3)
print("阶乘结果：",result)