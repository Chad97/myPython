# 函数注释方法根据PE8代码风格函数定义要距离上下文2个换行
def say_hello():
    """
    打招呼
    """
    print('hello')


# Ctrl + q 查看函数定义注释


def sum_2_number(num1, num2, count):
    """打印多行hello

    :param num1: 第一个数字
    :param num2: 第二个数字
    :param count: 打印的东西
    """
    row = 0
    while row < count:
        say_hello()

        row += 1

    print("%d + %d = %d"%(num1, num2, num1 + num2))
    return num1 + num2


res = sum_2_number(3, 3, 5)
print(res)