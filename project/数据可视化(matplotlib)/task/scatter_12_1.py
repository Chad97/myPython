#  数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值
import matplotlib.pyplot as plt

x_s = list(range(1, 5000))
y_s = [x**3 for x in x_s]

plt.scatter(x_s, y_s, edgecolor='none', s=40, c=x_s)

plt.show()

