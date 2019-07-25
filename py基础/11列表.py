# 列表
list_name = ['小麦', '高粱', '大米']
# 1. 取索引,传输的书记不再列表中会报错
print(list_name.index('大米'))

# 2. 修改
list_name[2] = 'aaa'

# 3. 增加
list_name.append("白面")  # 列表末尾作家书记

list_name.insert(2, '123')  # 指定索引插入数据

temp_list = ['1','2','3']

list_name.extend(temp_list)  # 把列表追加到列表末尾


# 4. 删除
# del（delete）这个关键字是用来将一个变量从内存中删除的
del list_name[2]
list_name.remove('小麦')  # 删除对象
list_name.pop(0)  # 默认删除最后一个，指定后删除对应索引
# list_name.clear()  # 清空列表

# 5. 统计
ll = len(list_name)  # 统计列表中列表的长度
print('长度为：%d'%ll)

cc = list_name.count('3')
print('3出现了%d次'%cc)

print(list_name)

# 6. 排序
num_list = [1,2,3]
str_list = ['a','b','c']


# 升序
num_list.sort()
str_list.sort()

# 降序
num_list.sort(reverse=True)
str_list.sort(reverse=True)


# 逆序（反转）
num_list.reverse()
str_list.reverse()
