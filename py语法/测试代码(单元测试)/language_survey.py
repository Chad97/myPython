from py_01测试类 import AnonymousSurvey


#  定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "你第一次说的语言是什么？"
my_survey = AnonymousSurvey(question)

#  显示问题并存储答案
my_survey.show_question()
while True:
    res = input('请输入答案：')
    if res == 'q':
        break
    my_survey.store_response(res)

#  显示调查结果
my_survey.show_results()
