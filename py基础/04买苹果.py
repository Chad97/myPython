price_str = float(input("苹果的价格"))
weight_str = float(input("苹果的重量"))



Total = price_str * weight_str
print('价格:%.02f,重量:%.02f,合计%.02f元'%(price_str, weight_str, Total))

'''
格式化字符串
%s 字符串
%d 有符号十进制，%06d 表示输出书记的整数显示位数，不足的地方用0补全
%f 浮点数 %.02f表示小数点后只显示2位小数
%% 输出 %
'''
name = '小明'
print('我的名字叫%s,请多多关照!'%name)

student_id = 2
print('我的学号是：%06d'%student_id)
# %%转义
scale = 0.66
print('占比是：%.02f%%'%(scale * 100))# 避免输出100次数字符串