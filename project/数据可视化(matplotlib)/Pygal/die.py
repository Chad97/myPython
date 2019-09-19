from random import randint

class Die():
    """ 表示一个骰子 """

    def __init__(self, num_sides=6):
        """ 骰子默认6面 """
        self.num_sides = num_sides

    def roll(self):
        """ 返回1和骰子面数直接的随机数 """
        return randint(1, self.num_sides)
