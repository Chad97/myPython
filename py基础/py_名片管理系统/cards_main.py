#! /usr/bin/python3
import cards_tools

while True:
    #  TODO(Chad) 显示功能菜单
    cards_tools.show_menu()
    action_str = input('请选择希望执行的操作：')
    print('您选择的是[%s]' % action_str)
    if action_str in ['1', '2', '3']:
        if action_str == '1':
            cards_tools.new_card()
        elif action_str == '2':
            cards_tools.show_card()
        elif action_str == '3':
            cards_tools.search_card()

    elif action_str == '0':
        print('欢迎再次使用名片管理系统')
        break
        #  退出系统 pass 表示一个占位符，能保证程序结构正确
        #  pass
    else:
        print('请输入的指令不正确，请重新输入')
