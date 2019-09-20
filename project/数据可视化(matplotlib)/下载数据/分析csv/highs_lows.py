import csv
from datetime import datetime
from matplotlib import pyplot as plt

""" enumerate
枚举一个可遍历的对象 返回 下标 和 对象，的哥个start 指定起始位置
"""

# 从文件中获取最高\低气温 和日期
filename = '.\data\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
       try:
           #  日期
           current_date = datetime.strptime(row[0], "%Y-%m-%d")
           #  最高温度
           high = int(row[1])
           #  低气温
           low = int(row[3])
       except ValueError:
           print(current_date, 'missing data')
       else:
           dates.append(current_date)
           highs.append(high)
           lows.append(low)

# 替换sans-serif字体
plt.rcParams['font.sans-serif'] = ['SimHei']

#  根据数据绘制图像
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()
#  设置图形格式
title = "2014年气温差"
plt.title(title, fontsize=20)


plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
