name = '小明'


def print_line(conut):
    """打印hello
    :param conut: 打印次数:
    :return: no
    """

    row = 0
    while row < conut:
        print('hello Python')
        row += 1


"""
- 不能以数字开头
- 不能和关键字重名

以数字开头 是无法在pycharm 中通过导入模块的
python 在使用 import 之后 会编译一个 .pyc 文件，是二进制文件 用来提高程序速度 
"""