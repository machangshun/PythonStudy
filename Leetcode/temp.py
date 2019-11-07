s = ["ling","yi","er","san","si","wu","liu","qi","ba","jiu"]
p = []
last = 0
p.append(input())
for i in p:
    last += int(i)
if last / 100 != 0:
    print("%s "%s[int(last/100)])
    print("%s "%s[int(last %100/10)])
elif last %100 /10 != 0:
    print("%s "%s[int(last%100/10)])
print("%s"%s[int(last%10)])


