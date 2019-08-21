import unittest
from py_Employee import Employee


class TestEmployee(unittest.TestCase):
    """ 测试雇员类 """
    def setUp(self):
        name = '张三'
        self.zs_Employee = Employee(name)

    def test_default_test(self):
        self.assertEqual('张三', self.zs_Employee.name)

    def test_add_salary(self):
        self.zs_Employee.give_raise(5000)
        self.assertEqual(15000, self.zs_Employee.salary)


if __name__=="__main__":
    unittest.main()
