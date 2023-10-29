# name="zhangchulan"
# for x in name:
#     print(x)
name = input("请输入一个值，来进行查询:")
count = 0
for x in name:
    if x == "j":
        count += 1
print(f"a有{count}个")
