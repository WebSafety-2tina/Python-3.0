##函数：是组织好的，可重复使用的，用来实现特定功能的代码段，python的内置函数
str1="zhangchulan"
str2="dadkjajkda"
str3="dadadadada"
#定义一个计数的变量
count=0
for i  in str1:
    count+=1
print(f'字符串{str1}的长度为:{count}')
count=0
for i  in str2:
    count+=1
print(f'字符串{str2}的长度为:{count}')
count=0
for i  in str3:
    count+=1
print(f'字符串{str3}的长度为:{count}')

#使用函数优化过程/函数特点:已经组织好的，可重复使用，针对特定功能
#减少重复性代码，提高开发效率
def my_len(data):
    count=0
    for i in data:
        count+=1
    print(f'字符串{data}的长度是{count}')
my_len(str1)
my_len(str2)
my_len(str3)