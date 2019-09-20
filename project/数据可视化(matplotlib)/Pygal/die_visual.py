from die import Die
import pygal


#  创建D6
die_1 = Die()
die_2 = Die(10)

#  掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#  分析结果计算 每个点出现的次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for val in range(2, max_result + 1):
    frequency = results.count(val)
    frequencies.append(frequency)

#  对结果进行可视化
hist = pygal.Bar()

hist.title = "掷D6骰子1000次分析"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "点数"
hist.y_title = "次数"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')

