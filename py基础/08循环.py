i = 0
while i < 5:
    print('hello py  %d'%i)

    i += 1


k = 0
result = 0
while k <= 10:
    if k % 2 == 0:
        result += k
    if k == 3:
        break # 跳出循环
    k += 1

print(result)


p = 0
while p < 5:
    if p == 3:
        p += 1
        # 只是条件成立这一次不执行，但是要注意计数器避免造成死循环
        continue

    print(p)

    p += 1

# 嵌套循环 打印9*9乘法表


def multiple_table():

    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print('%d x %d = %d ' % (row, col, row * col), end="\t")

            col += 1

        print('\n')
        # 在每一行输出完毕的末尾增加一个换行
        row += 1

# 转义字符 \
# \n 换行 \t 横向制表符 \r 回车


'''
赋值运算符
=	    简单的赋值运算符	    c = a + b 将 a + b 的运算结果赋值为 c
+=	    加法赋值运算符	    c += a 等效于 c = c + a
-=	    减法赋值运算符	    c -= a 等效于 c = c - a
*=	    乘法赋值运算符	    c *= a 等效于 c = c * a
/=	    除法赋值运算符	    c /= a 等效于 c = c / a
%=	    取模赋值运算符	    c %= a 等效于 c = c % a
**=	    幂赋值运算符	        c **= a 等效于 c = c ** a
//=	    取整除赋值运算符	    c //= a 等效于 c = c // a

'''
