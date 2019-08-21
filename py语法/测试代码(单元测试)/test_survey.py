import unittest
from py_01测试类 import AnonymousSurvey

"""  setUp()
setUp() ，Python将先运行它，再运行各个以test_打头的方法。这样，在你编写的每个测试方法中都可使用在方法setUp() 中创建的对象了。
"""


class TestAnonymousSurveySurvey(unittest.TestCase):
    """ 针对AnonymousSurvey的类测试 """

    def setUp(self):
        """ 创建一个调查对象和一组答案，供使用测速方法使用 """
        question = '你第一次使用的语言是？'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['中文', '西班牙语', '英语']

    def test_store_single_response(self):
        """ 测试单个答案储存 """
        self.my_survey.store_response(self.responses[0])
        self.assertIn('中文', self.my_survey.responses)

    def test_store_three_responses(self):
        for res in self.responses:
            self.my_survey.store_response(res)

        for res in self.responses:
            self.assertIn(res, self.my_survey.responses)


unittest.main()
