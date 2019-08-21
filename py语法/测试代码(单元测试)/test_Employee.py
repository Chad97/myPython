import unittest
from py_Employee import Employee


class TestEmployee(unittest.TestCase):
    """ 测试雇员类 """
    def setUp(self):
        name = '张三'
        self.zs_Employee = Employee(name)

    def default_test(self):
        self.assertEqual('张三', self.zs_Employee.name)

    def add_salary(self):
        self.zs_Employee.give_raise(3000)
        self.assertEqual(13000, self.zs_Employee.re_salary)


unittest.main()
