hello_str = 'hello word'

print(hello_str.startswith('Hello'))  # 区分大小写

print(hello_str.endswith('word'))

# index 查找不存在直接报错，find会返回-1
print(hello_str.find('llo'))
# print(hello_str.index('ww'))

print(hello_str.replace('word','python'))  # 不会修改原有字符串
print(hello_str)

str = '0123456789'
print(str[1:])
print(str[1::2])
print(str[2:-1])
print(str[-2:])
print(str[::-1])  # 利用切片反转