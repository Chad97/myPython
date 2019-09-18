import matplotlib.pyplot as plt

x_val = list(range(1, 1000))
y_val = [x**2 for x in x_val]

plt.scatter(x_val, y_val, edgecolor='none', s=40, c=y_val)

plt.title('Square', fontsize=21)
plt.xlabel('value', fontsize=12)
plt.ylabel('count', fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=12)

#  保存到当前路径 去除空白边
plt.savefig('test_save.png', bobx_inches='tight')
plt.show()

# 动手试一试
# 15-1 立方 ：数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。
