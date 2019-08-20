import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像 张 三 这样的姓名吗？"""
        formatted_name = get_formatted_name('张', 'alic')
        self.assertEqual(formatted_name, '张 Alic')
        """
            创建了一个测试用例，使用断言 assertEqual 来测试结果
        """
    #  添加新的测试
    def test_first_middle_last_name(self):
        """ 能正确处理 ABB 这样的姓名吗 """
        formatted_name = get_formatted_name('a', 'b', 'b')
        self.assertEqual(formatted_name, 'A B B')


unittest.main()
