'''
02-列表的嵌套
'''
citys = [["南京市","苏州市","无锡市"],["杭州","台州"]]
for city in citys:
    for ct in city:
        print(ct)
print("="*50)
i = 0
while i < len(citys):
    j = 0
    while j < len(citys[i]):
        print(citys[i][j])
        j += 1
    i += 1
