age=int(input("请输入你的年龄："))
print(f"你确定你已经{age}岁了吗")
if age>=18:
    print("你尽然已经成年了，那我就给你我的珍品吧")
elif age<18:
    print("未成年禁止访问,滚")
else:
    print("你要干什么")

print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age1 = int(input("请输入你的年龄:"))
if age >= 18:
    print("您已成年，游玩需要补票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快")

print("欢迎来到动物园")
shengao = int(input("请输入你的身高(单位:cm):"))
if shengao >= 150:
    print("您已经超过限制身高，应按照正常收费")
elif shengao <= 149:
    print(f"您的身高为{shengao},可以免票进入")
else:
    print("您输入错误，无法进行计算")

print("欢迎你进入")
if int(input("请输入你的年龄:")) <= 150:
    print("身高低于150，可以免费")
elif int(input("请输入你的VIP等级:")) > 5:
    print("年龄大于5岁，可以免费")
elif int(input("请告诉我今天是几号")) == 1 > 1:
    print("今天是1号可以免费")
    print("今天不是1号，不免费")
else:
    print("你好")
