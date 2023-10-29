print("欢迎来到动物园")
if int(input("请输入你的身高:")) > 123:
    print("你的身高大于123cm，不可以免费")
    print("如果你的vip等级大于3，你仍然可以免费进入")
    if int(input("请告诉我你的vip等级:")) > 3:
        print("恭喜你，你的VIP等级大于3，可以免费游玩")
    else:
        print("对不起，您需要补票(10元)")
else:
    print("欢迎你小朋友，可以免费")
