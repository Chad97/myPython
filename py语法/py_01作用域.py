#  全局变量
num = 10

"""
在python中是不允许在局部作用域中直接使用赋值语句修改全局变量，
进行修改的只会在局部中定义一个新的局部变量
"""


def demo1():
    num = 100
    print('demo1 => %d' % num)


def demoTest():
    print('demoTest => %d' % num)
"""
global 声明全局变量
"""
def demo2():
    global num
    num = 99
    print('demo2 => %d' % num)


def demo3():
    print('demo2=3 => %d' % num)


demo1()
demoTest()
demo2()
demo3()


#  代码结构示意图
"""
    shebang
    import
    全局变量
    函数定义
    执行代码
"""