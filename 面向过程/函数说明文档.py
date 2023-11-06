#给函数添加说明文档，辅助理解函数的作用
def add(x,y):
    """
    add函数可以接受2个参数，进行2数相加的功能
    :param x: 形参x便是相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值2数相加的结果
    """
    result=x+y
    print(f'{result}')
    return result
add(5,6)