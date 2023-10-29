import random

num1 = random.randint(1, 10)
if int(input("请猜一个数字:")) == num1:
    print("才对了，你我心连心")
elif int(input("再猜一次:")) == num1:
    print("猜对了，真不容易")
elif int(input("又错了，再来一次:")) == num1:
    print("终于猜对了，唉")
else:
    print(f"机会用完了，你真笨,答案为{num1}")
