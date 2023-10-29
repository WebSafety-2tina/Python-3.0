##两层循环 外层100  内层10
i = 1
while i <= 100:
    print(f"今天是{i}天")
    ##内层循环变量
    j = 0
    while j < 10:
        print(f"送出去的{j}只")
        j += 1
    print("xxxx")
    i += 1
print(f"第{i - 1}天，结束")
