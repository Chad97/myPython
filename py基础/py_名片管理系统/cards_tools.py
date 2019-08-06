# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print('*' * 50)
    print('\n欢迎使用【名片管理系统】v1.0\n')
    print('1. 新增名片')
    print('2. 显示名片')
    print('3. 搜索名片\n')
    print('0. 退出系统')
    print('*' * 50)


def new_card():

    """新增名片"""
    print('-' * 100)
    print('新增名片')
    name_str = input('请输入姓名：')
    tel_str = input('请输入电话：')
    qq_str = input('请输入qq：')
    email_str = input('请输入邮箱：')

    card_dict = {
        "name": name_str,
        "tel": tel_str,
        "qq": qq_str,
        "email": email_str
    }
    card_list.append(card_dict)
    print(card_dict)
    print('添加%s名片成功 !' % name_str)


def show_card(list = card_list):
    """显示名片"""
    print('-' * 100)
    print('显示所有名片')
    #  判断是否存在名片记录
    if len(list) == 0:
        return print('当前没有任何信息，请使用新增功能添加名片 !')

    #  输出表头
    for title in ['姓名', '电话', 'QQ', '邮箱']:
        print(title, end="\t\t")
    print("")
    print("=" * 50)
    #  输出列表信息
    for item in list:
        print('%s\t\t%s\t\t%s\t\t%s' % (item["name"], item["tel"], item["qq"], item["email"]))


def search_card():
    """删除名片"""
    print('-' * 100)
    print('查询名片')

    check_list = []
    check_obj = input('请输入要查找的名片：')
    for item in card_list:
        if item['name'] == check_obj:
            check_list.append(item)
            #  调用显示当前名片
            show_card(check_list)
            #  调用处理名片
            deal_card(item)
            break
    else:
        print('没有找到 %s ' % check_obj)


def deal_card(list):
    """处理找到的名片

    :param list: 传入找到的名片对象
    :return: void
    """
    action_str = input('请输入对名片的操作 [1]: 修改 / [2]：删除 / [0]：返回上级')
    if action_str == "1":
        for new_val in list:
            #  list[new_val] = input('请输入%s：' % new_val)
            list[new_val] = input_card(list[new_val], '请输入%s： ' % new_val)

        print('修改成功！')
    elif action_str == "2":
        card_list.remove(list)
        print('删除成功！')


def input_card(old_valve, message):
    """输入名片信息

    :param old_valve: 字段中原有的值
    :param message: 用户输入的新值
    :return: 用户输入了内容返回内容否则返回原有值
    """
    result_str = input(message)
    if len(result_str) > 0:
        return result_str
    else:
        return old_valve
