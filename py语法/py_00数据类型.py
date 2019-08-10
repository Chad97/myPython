"""不可变数据类型"""
# 数字 int, bool, float, complex
# 字符串 str
# 元组 tuple

"""可变数据类型"""
# 列表
# 字典

a = [1, 2, 3]
print(id(a))
a.append(99)
print(a)
print(id(a))

key = (1,'k',True)

Dictionary = {
    key: '元组可以作为字典的key'
}
print(Dictionary)

#  哈希
"""
接收一个不可变类型作为参数
返回一个整数
哈希是一种算法,其作用是提取数据的特征码
相同的内容 得到 相同的结果
不同的内容 得到 不同的结果
在py中，设置字典的键值对，会首先对key进行 hash 处理已决定如何在内存中保存字典数据，以方便后续的CRUD

"""