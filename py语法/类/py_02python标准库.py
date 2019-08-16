from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['张三'] = 'java'
favorite_languages['李四'] = 'C'
favorite_languages['王五'] = 'python'
favorite_languages['赵二'] = 'ruby'

for name,language in favorite_languages.items():
    print(name + '喜欢的语言：' + language + '.')


"""
9-14 骰子 ：模块random 包含以各种方式生成随机数的函数，其中的randint() 返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：
请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数。创建一个6面
的骰子，再掷10次。 创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
"""


class Die():
    def __init__(self):
        self.side = 6

    def roll_die(self, count):
        """抛出筛子"""
        i = 0
        print('开始抛出[%d]面骰子【%d】次' % (self.side ,count))
        while i < count:
            print('本次点数是：[%d]' % randint(1, self.side))

            i += 1


start_game = Die()
start_game.roll_die(10)
start_game.side = 10
start_game.roll_die(10)
start_game.side = 20
start_game.roll_die(10)

