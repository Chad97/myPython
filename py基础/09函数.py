# 函数注释方法根据PE8代码风格函数定义要距离上下文2个换行
def say_hello():
    """打招呼"""
    print('hello')


# Ctrl + q 查看函数定义注释
say_hello()


def sum_2_number(num1, num2):
    print("%d + %d = %d"%(num1, num2, num1 + num2))
    return num1 + num2


res = sum_2_number(3,3)
print(res)