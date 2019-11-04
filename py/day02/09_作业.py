"""
1.输入命令选择菜单选项
========================
1.土豆牛肉盖浇饭
2.青椒土豆丝盖浇饭
3.
========================
请选择食物：1
========================
1.土豆
2.牛肉
3.饭
=======================
请选择添加食物：1
注意事项：
1.保留 后期整体上交
2.录制视频 上传群
"""
print("输入命令选择菜单选项")
print("="*30)
print("1.土豆牛肉盖浇饭\n2.青椒土豆丝盖浇饭\n3.番茄炒蛋盖浇饭")
print("="*30)
choose = int(input("1.请选择食物："))
if choose == 1:
    print("="*30)
    print("1.土豆")
    print("2.牛肉")
    print("3.饭")
    print("="*30)
    choose_1 = int(input("2.请选择添加食物："))
    if choose_1 == 1:
        print("土豆牛肉盖浇饭多加土豆")
    elif choose_1 == 2:
        print("土豆牛肉盖浇饭多加牛肉")
    else:
        print("土豆牛肉盖浇饭多加饭")
elif choose == 2:
    print("=" * 30)
    print("1.青椒")
    print("2.土豆丝")
    print("3.饭")
    print("=" * 30)
    choose_1 = int(input("2.请选择添加食物："))
    if choose_1 == 1:
        print("青椒土豆丝盖浇饭多加青椒")
    elif choose_1 == 2:
        print("青椒土豆丝盖浇饭多加土豆丝")
    else:
        print("青椒土豆丝盖浇饭多加饭")
elif choose == 3:
    print("=" * 30)
    print("1.番茄")
    print("2.蛋")
    print("3.饭")
    print("=" * 30)
    choose_1 = int(input("2.请选择添加食物："))
    if choose_1 == 1:
        print("番茄炒蛋盖浇饭多加番茄")
    elif choose_1 == 2:
        print("番茄炒蛋盖浇饭多加蛋")
    else:
        print("青椒土豆丝盖浇饭多加饭")

