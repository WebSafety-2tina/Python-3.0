n=int(input("请输入一个整数:"))
m=0
for i in range(1,n+1):
    if i%2==0:
        m-=i
    else:
        m+=i
print(m)