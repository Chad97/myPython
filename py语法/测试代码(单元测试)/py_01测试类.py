#  unittest.TestCase 提供了很多断言方法 常用的如下


""" 各种断言方法
assertEqual(a, b)       核实 a == b
assertNotEqual(a, b)        核实 a != b
assertTrue(x)       核实 x 为True
assertFalse(x)      核实 x 为False
assertIn(item, list)        核实 item 在 list 中
assertNotIn(item, list)     核实 item 不在 list 中
"""


class AnonymousSurvey():

    """ 收集匿名调查问卷答案 """
    def __init__(self, question):
        """ 储存一个问题，并为储存答案做准备 """
        self.question = question
        self.responses = []

    def show_question(self):
        """ 显示调查问卷 """
        print(self.question)

    def store_response(self, new_responense):
        """ 储存单份调查问卷 """
        self.responses.append(new_responense)

    def show_results(self):
        """ 显示收集到的所有答卷 """
        print('所有答卷是：')
        for rs in self.responses:
            print('- ' + rs)


AA = AnonymousSurvey('asdasd')
AA.show_question()