names = {"name":"张学友","sex":"男","age":18}
for key in names.keys():
    print("key:",key)

for value in names.values():
    print("value:",value)

for item in names.items():
    print("item:",item)

for key,value in names.items():
    print("%s:%s"%(key,str(value)))