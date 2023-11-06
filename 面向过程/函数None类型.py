##None:空的，无实际意义
def say_hello():
    print("hello...")
result=say_hello()
print(f'返回的内容是{result}')
print(f'返回的内容是{type(result)}')


def sat_hello2():
    print("你好啊")
    return None #通过return返回Nnoe   在实际运用是，可以返回空返回值
##在if语句中，None相当于False,一般用于在函数中主动返回None，配合if判断做相关处理
result=sat_hello2()
print(f'{result}')
print(f'{type(result)}')


def n_age(age):
    if age>18:
        return "SUCCESS"
    else:
        return None
result=n_age(16)
if not result:
    print("未成年，不可以进入")