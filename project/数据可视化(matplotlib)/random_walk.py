from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """ 生成随机漫步的类 """

    def __init__(self, num_points=5000):
        """ 初始化随机漫步属性 """
        self.num_points = num_points

        #  所有的漫步都始于 0, 0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 计算随机漫步所有的点 """

        #  不断漫步，直到到达指定长度
        while len(self.x_values) < self.num_points:

            #  决定前进方向 以及前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #  拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #  计算下一个点的x和y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
