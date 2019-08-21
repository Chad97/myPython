"""
动手试一试
11-3 雇员 ：编写一个名为Employee 的类，其方法__init__() 接受名、姓和年薪，并将它们都存储在属性中。编写一个名为give_raise() 的方法，它默认将
年薪增加5000美元，但也能够接受其他的年薪增加量。
为Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise() 和test_give_custom_raise() 。使用方法setUp() ，以免在
每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了。
"""


class Employee():
    """ 雇员 """
    def __init__(self, name, salary=10000):
        self.name = name
        self.salary = salary

    def give_raise(self, count=5000):
        """ 加工资 """
        self.salary += count

    def print_salary(self):
        """ 打印工资 """
        print('%s 的 工资是： %d' % (self.name, self.salary))


