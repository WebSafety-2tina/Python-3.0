i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

import random

num = random.randint(1, 100)
count = 0
# 通过一个布尔类型的变量，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜测数字"))
    count += 1
    if guess_num == num:
        print("正确")
        flag = False  ##设置为false就是终止循环的条件
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")
print(f"你总过猜测了{count}次数")
