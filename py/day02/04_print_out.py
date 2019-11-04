'''
01-输入输出
'''
'''
1.输出
1.1普通输出
1.2格式化输出 添加变量
1.3换行输出
'''
#普通
print("dd")
#格式化
'''
%s字符串占位符
%d整型占位符
%f 浮点型占位符
%C 字符占位符
'''
age = 18
name = "mac"
print("我叫%s，我今年%d岁"%(name,age))

#换行输出
print("的地得\n的地得")
name = "machangshun"
qq = "2542691072"
iphone = "15150678100"
addr = "南航金城"
print("="*20)
print("姓名：%s\nQQ:%s\n手机号：%s\n公司：%s"%(name,qq,iphone,addr))
print("="*20)

'''
2.输入
2.1输入函数raw_input() python2.x版本可以使用
2.2输入函数input()任何版本
注意事项：input函数默认字符串类型
'''
name = input("请输入您的姓名：")
phone = input("请输入您的电话：")
qq = input("please input your qq:")
print("="*30)
print("姓名：%s\n电话：%s\nQQ:%s"%(name,phone,qq))
print("="*30)