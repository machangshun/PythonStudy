i = 0
while i < 10:
    #break 终止循环
    #continue跳出一次循环执行下一次循环
    #注意事项：
    #作用域：当前所在循环体
    j = 0
    while j < i:
        break
    i += 1