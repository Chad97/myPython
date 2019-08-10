list = [1, 2, 3]
num = 10

# def numTest(list):
#     list = [4, 5, 6]
def numTest(list):
    list.append(99)
    print(list)

"""
方法会改变外部参数，赋值不会
"""
numTest(list)
print(list)


def demo(num):
    num += num
    print(num)


demo(num)

"""
如果 是数组使用+= （相加在赋值）并不是使用+=，而是调用了extend （合并2个数组）
故而 影响了外部数据
"""
demo(list)
print(list)


#  缺省参数应定义在末尾
def print_info(name, title='是', gender=True):
    """

    :param title: 是
    :param name: 姓名:
    :param gender: True: 男 False: 女
    :return: None
    """
    gender_text = '男'
    if not gender:
        gender_text = "女"

    print('小明 %s %s' % (title, gender_text))


print_info('小明')
#  指定缺省值参数
print_info('小红', gender=False)

##  多值参数
#  *是元组
#  **是字典
def most_demo(num, *age, **obj):
    print(num)
    print(age)
    print(obj)

# most_demo(1)
most_demo(1, 2, 3, name='小明', age=18)

def sum_numbers(*args):
    num = 0
    for n in args:
        num += n
    return num


result = sum_numbers(1, 2, 3)
print(result)


