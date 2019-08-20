import unittest
from city_func import city_func


class CityTestCase(unittest.TestCase):
    """ 测试国家和城市 拼接 """
    def test_city(self):
        city_name = city_func('中国', '上海')
        self.assertEqual(city_name, '中国 上海')

    def test_city1(self):
        city_name = city_func('加拿大', '温哥华')
        self.assertEqual(city_name, '加拿大 温哥华')


unittest.main()