for i in range(10):  ##continue中断本次循环 跳出本次循环，执行下次循环，分内层循环和外层循环
    if i%2==0:
        continue
    print(i)