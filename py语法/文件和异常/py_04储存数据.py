import json
#  函数json.dump() 接受两个实参：要存储的数据以及可用于存储数据的文件对象。下面演示了如何使用json.dump() 来存储数字列表
numbers = [2, 3, 4, 5, 6, 123]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


#  使用load 把数据读到内存中
with open(filename) as f:
    nums = json.load(f)

print(nums)

# username = input('请输入用户名：')
#
# with open('username.json', 'w') as f:
#     json.dump(username, f)
#     print('储存成功 !')


def get_stored_username():
    file_name = 'username.json'
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None

    else:
        return username


def new_username():
    username = input('请输入用户名：')
    file_name = 'username.json'
    with open(file_name, 'w') as f:
        json.dump(username, f)
        print('储存成功')


def greet_user():
    """ 向用户打招呼 """
    username = get_stored_username()

    if username:
       print('欢迎 %s ~' % username)
    else:
        new_username()


greet_user()


