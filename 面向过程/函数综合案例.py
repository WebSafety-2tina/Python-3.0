money=5000000
name=input("请输入您的姓名:")
def chaxun(show_hed):
    if show_hed:
            print("------------查询余额------------")
    print(f'{name}，您好，您的余额剩余:{money}元')
def saving(num):
    global money
    money+=num
    print("------------存款------------")
    print(f'{name}您好,您存款{num}元成功')
    chaxun(False)
def get_money(num):
    global money
    money-=num
    print("----------取款---------")
    print(f'{name},您好，您取款{num}元成功.')
    chaxun(False)
def main():
    print("----------主菜单---------")
    print(f'{name},您好，欢迎来到银行')
    print("查询余额\t[输出1]")
    print("存款\t\t[输出2]")
    print("取款\t\t[输出3]")
    print("退出\t\t[输出4]")
    return input("请输入您的选择:")
while True:
    keyboard_input=main()
    if keyboard_input=='1':
        chaxun(True)
        continue
    elif keyboard_input=='2':
        num=int(input("您想要存多少钱?请输入:"))
        saving(num)
        continue
    elif keyboard_input=='3':
        num=int(input("您想要取多少钱？请输入:"))
        get_money(num)
        continue
    else:
        print("程序结束")
        break
