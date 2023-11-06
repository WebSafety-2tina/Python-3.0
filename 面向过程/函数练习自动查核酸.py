def check(num):
    num=float(num)
    if num<=37.5:
        print(f'体温测量中，您的体温为{num}°,体温正常')
    else:
        print(f'体温测量中，您的体温为{num}°，体温不正常，需要隔离!')
check(input("请输入您的体温:"))
