# 元组

"""
元组用()定义
元组不能修改
元组从索引０开始
"""

my_tuple = 1.2,'asd','aa',3
print(my_tuple[1])

st = single_tuple = (1,)
print(type(st))
"""
定义单元素的元组要加　,　不然就会默认解释其中的元素
"""
# 同样拥有　取索引和统计的方法
my_tuple.index('aa')
my_tuple.count('aa')

# 格式化字符串也是元组
print('%s 年龄是　%d 身高是　%.2f' % ('小米', 18,1.75))