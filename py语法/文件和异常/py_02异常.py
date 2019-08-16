try:
    print(5/0)

except ZeroDivisionError:
    print('错误处理')


#  计算2个数的商
# while True:
#     first_num = input('请输入除数(q 退出)：')
#     if first_num == 'q':
#         break
#     second_num = input('请输入被除数：')
#
#     try:
#         answer = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print('不能除以0！')
#     else:
#         print(answer)


#  处理FileNotFoundError 异常
try:
    with open('asd.txt') as f:
        contents = f.read()
except FileNotFoundError:
    print("找不到这个文件")
else:
    print(contents)
