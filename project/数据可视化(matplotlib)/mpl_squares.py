import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
#  设置图标标题并给坐标轴加上标签
plt.title("squares Number", fontsize=23)
plt.xlabel('time', fontsize=12)
plt.ylabel('count', fontsize='12')

#  设置刻度标记大小
plt.tick_params(axis='both', labelsize=12)

plt.show()
