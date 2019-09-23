#  这是一个生成用户github-commit 数的 统计
import requests
import pygal
import sys

#  执行API调用并存储响应
user_name = input('请输入用户名:')

url = 'https://ruoduan.cn:8888/user-info?name=' + user_name
r = requests.get(url)
print("Status code:", r.status_code)

try:
    user_data = r.json()
except ValueError:
    print('请输入正确的用户名')
    sys.exit()

repoCommitCount = user_data['repoCommitCount']
repoCommitCountDescriptions = user_data['repoCommitCountDescriptions']

names, plot_dicts = [], []
for item, key in repoCommitCount.items():
    names.append(item)

    plot_dict = {
        'value': key,
        'label': repoCommitCountDescriptions[item] if repoCommitCountDescriptions[item] else " "
    }
    plot_dicts.append(plot_dict)

chart = pygal.Bar()
chart.title = 'github-commit仓库统计图'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('hn_submissions.svg')