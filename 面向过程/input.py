# ##print输出语句     Input输入的内容
# name=input("请告诉我你是谁：")
# print("尊敬的：%s"%name)
# num=input("尊敬的%s先生,请输入你的银行卡号码:"%name)
# num=int(num)
# print("你的银行卡类型是",type(num))


user_name=input("请输入你的名字:")
if user_name=="张楚岚":
    user_type="ssssvip"
else:
    print("不是SSSSSVIP，无法进入")
    exit(0)
print("您好:",user_name,"您是尊贵的:",user_type,"用户,欢迎您的光临")
