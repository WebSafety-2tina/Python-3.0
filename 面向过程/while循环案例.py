i = 1
while i <= 9:
    # 定义内层循环变量
    j = 1
    while j <= i:
        print(f"{j}x{i}={j * i}\t", end="")
        j += 1

    i += 1
    print()
