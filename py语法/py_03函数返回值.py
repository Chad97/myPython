def checkReturn():
    temp = 10
    wetness = 20
    #  返回多个值使用元组 可以不加括号
    return temp, wetness


#  变量个数要和元组保持一致
gl_e, gl_we = checkReturn()


print(gl_e)
print(gl_we)
