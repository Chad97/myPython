"""遍历字典"""
user_0 = {
    'a': 'zs',
    'c': 'enrico',
    'b': 'fermi',
    }

for k, v in user_0.items():
    print('\nKey  ' + k)
    print('value  ' + v)

# 当我们只需要键 不需要值的时候
for key in user_0.keys():
    print('键%s' %key)

# 当我们只需要值不需要键的时候
for value in user_0.values():
    print('值%s' %value)

# 按顺序遍历字典 值反之
for k in sorted(user_0.keys()):
    print('排序%s' %k)

languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


# 在遍历字典的时候使用set去重
print('去重后：')
for lan in set(languages.values()):
    print(lan.title())


alien = {
    'x': 0,
    'y': 10,
    'speed': 'medium'
}

# 向左移动外星人 根据其速度决定距离
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# 新的位置 = 老位置 + 增量
alien['x'] = alien['x'] + x_increment

print('new alien is', alien)

# 删除键-值对
alienTow = {
    'name': '阿三',
    'sex': '1'
}

del alienTow['sex']
print(alienTow)
# {'name': '阿三'}

# 在字典中储存列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, lans in favorite_languages.items():
    print('\n%s喜欢的是: ' % name.title())
    for language in lans:
        if len(language) != 1:
            print(language.title())
        else:
            print('比较专一只有：%s' % language.title())

