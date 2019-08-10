#  交换2个变量不使用其他变量
a = 6
b = 100

#  1. 使用其他变量的
"""
c = a
a = b
b = c
"""

#  2. 解法1

# a = a + b
# b = a - b
# a = a - b

#  3. 解发2  python 专有 右边是一个元组
#  a, b = (b, a)
a, b = b, a

print(a,b)