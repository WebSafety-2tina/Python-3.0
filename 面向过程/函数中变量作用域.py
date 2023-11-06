##变量的作用域，是变量的作用范围，分别为局部变量和全局变量
#局部变量，在函数体内部的变量，即只在函数内部生效
def ter1_a():
    num=100
    print(num)
ter1_a()
#全局变量，在函数体内，外都能生效的变量
num=200
def ter_a():
    print(f'test_a:{num}')
def ter_b():
    print(f'test_b:{num}')
ter_a()
ter_b()
print(num)

##global变量值
num=200
def ter_a():
    print(f'test_a:{num}')
def ter_b():
    global num   ##设置内部定义的变量为全局变量
    num=500
    print(f'test_b:{num}')
ter_a()
ter_b()
print(num)