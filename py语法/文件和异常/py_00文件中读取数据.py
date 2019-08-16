"""  TODO 注意 with和close()
关键字with 在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了open() ，但没有调用close() ；你也可以调用open() 和close() 来打开和关闭文件，但
这样做时，如果程序存在bug，导致close() 语句未执行，文件将不会关闭。这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调
用close() ，你会发现需要使用文件时它已关闭 （无法访问），这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可
让Python去确定：你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。
"""
file_path = 'pi_digits.txt'

with open(file_path) as file_obj:
    contents = file_obj.read()
    print(contents.rstrip())
"""
相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空行呢？因为read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一
个空行。要删除多出来的空行，可在print 语句中使用rstrip() ：
"""

#  逐行读取
with open(file_path) as file_obj:
    for line in file_obj:
        print(line.rstrip())


#  一百万位的圆周率
filename = 'pi_million_digits.txt'
#  创建一个包含文件各行内容的列表
with open(filename) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

#  只显示32位
print(pi_string[:32] + "...")
print(len(pi_string))

#  圆周率值中包含你的生日吗?
with open(filename) as file_obj:
    lines = file_obj.readlines()

pi_str = ''
for line in lines:
    pi_str += line.rstrip()

birthday = input('请输入的生日mmddyy：')
if birthday in pi_str:
    print('你的生日出现在圆周率百万位~')
else:
    print('你的生日没有出现在圆周率百万位~')