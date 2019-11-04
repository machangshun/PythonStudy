'''
01-面向对象

'''

stu_a = {
    "name":"杨过",
    "age":28,
    "sex":"男",
    "home":"终南山"
}
stu_b = {
    "name":"小龙女",
    "age":18,
    "sex":"男",
    "home":"古墓"
}
stu_c = {

}

def stu_info(info):
    print("我是%s,今年%d,我是%s,我在%s"%(info["name"],info["age"],info["sex"],info["home"]))
stu_info(stu_a)
stu_info(stu_b)
'''
面向过程：数据和方法分开的 就是面向过程的编程
面向对象：数据和方法封装在一起 就是面向对象的编程
一切皆对象
'''