'''
1.
'''
print("="*30)
num = [5,4,2,3,1]
print(max(num))
print(min(num))
print("="*30)
str_ = "helloworld"
temp = ""
for i in str_:
   if i not in temp:
        temp += i
        print("%s:%d" % (i, str_.count(i)),end = ",")
print("")
print("="*30)
paths = []
while True:
    path = input("请输入路径：")
    if path == "exit":
        break
    else:
        paths.append(path)
strs = "/"
print("/"+strs.join(paths))