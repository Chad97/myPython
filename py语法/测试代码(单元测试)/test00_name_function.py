import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像 张 三 这样的姓名吗？"""
        formatted_name = get_formatted_name('张', 'alic')
        self.assertEqual(formatted_name, '张 Alic')


unittest.main()
