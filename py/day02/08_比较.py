'''
== != >= <= > <
'''
age = 18
height = 175
weight = 110
sex = "女"

#条件表达式
if sex == "女":
    pass
    if age == 18:
        pass
        if height == 175:
            pass
            if weight <= 110:
                pass

'''
逻辑运算符  and or not

'''
#封装 多态 继承 抽象
age = input("please input age:")
age = int(age)
if sex == "男" and 18 >= age >= 11 or False:
    print("ok!")
else:
    print("no!")