age = int(input("请输入你的年龄:"))
year = int(input("请输入你的入职的年份:"))
level = int(input("请输入你的级别:"))
if age >= 18:
    print("您已经成年")
    if age < 30:
        print("您的年龄达标")
        if year > 2:
            print(f"入职年龄超过{year}年，满足条件，可以领取")
        else:
            print(f"入职年龄不超过{year}年，不可以领取")
    elif level > 3:
        print(f"您的级别已经达到{level},满足条件达标")
    else:
        print(f"您的级别为{level}不达标，请继续努力")
else:
    print(f"年龄为{age},识别为未成年，不可进入公司，请呆在原地，等待工作人员")
