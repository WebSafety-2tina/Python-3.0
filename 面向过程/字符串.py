##字符串的三种定义方式
name="张楚岚"
print(type(name),name)
name2='张楚岚2'
print(type(name2),name2)
name3="""张楚岚3"""
print(type(name3),name3)
#在字符串内，包含双引号
hacker="张楚岚"
#在字符串内，包含引号
web="'Marco'"

##字符串的拼接
print("张楚岚"+"Marco")
print("学it来黑马"+"月入过万")
namr4="张楚岚"
address="19"
tel=10000000000000
print("我是",name,"我今年",address,"岁",tel)


##字符串格式化  占位符
#字符串为%s   整数为%d 浮点数为%f
#占位拼接
name5="张楚岚"
age=19
message="我叫%s,我今年%s岁"%(name5,age)
print(message)
#通过展位完成数字和字符串的拼接
class_num=57
ave_num=16781
nesss="周口职业技术学院%s班级，我的学号为%s"%(class_num,ave_num)
print(nesss)

name5="北京大学"
setup_year=2022
stock_price=19.99
message_num="我来自%s,我的年级为%d，我的钱包为%f"%(name5,setup_year,stock_price)
print(message_num)


num1=11
num2=11.321
print("数字11宽度限度5，结果为：%5d"%num1)
print("数字11宽度为1魏国为：%1d"%num1)
print("数字11.76宽度先付为7，小数为2结果为：%.2f"%num2)
##简便方式
print(f"我是{num1}，我今天的股票为{num2}")

#字符串格式化
print(f"18*11的结果为:{18*11}")
print(f"字串的类型是:%s"%type("字符串"))


#练习
name="周口职业技术有限公司"
stock_price=19.99
stock_code="003032"
stock_prie_daily_growth_factor=1.2
gorwth_days=15
print(f"公司：{name},股票代码{stock_code},当前股价{stock_price}")
num1222="每日增长系数为:%f,经过%d天的增长后，股票达到了：%f"%(stock_prie_daily_growth_factor,gorwth_days,(stock_price+stock_price*stock_prie_daily_growth_factor*gorwth_days))
print(num1222)
