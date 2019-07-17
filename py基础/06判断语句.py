age = int(input("请输入年龄: "))

if age >= 18:
    print('成年')
else:
    print('未成年')

print('你的年龄是：%d'%(age))

'''
逻辑运算符
与and/或or/非not
'''


if (age >=0 and age <=50):
    print('年龄在120之间')
else:
    print('年龄不在120之间')


python_score = 99
c_score = 50

if python_score > 60 or c_score > 60:
    print('ok')
else:
    print('no')

is_employee = False

if not is_employee:
    print('不是员工')

holiday_name = '平安夜'
if holiday_name == '情人节':
    print('买玫瑰，看电影')
elif holiday_name == '平安夜':
    print('买苹果')
elif holiday_name == '端午节':
    print('吃粽子')
else:
    print('其他节日')

# if嵌套 模拟安检
has_ticket = True
knife_lenght = 20

if has_ticket:
    if knife_lenght <= 20:
        print('允许上车')
    else:
        print('刀具超过20cm')

else:
    print('请购票')