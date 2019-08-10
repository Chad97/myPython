# def recursion(num):
#     if num > 10:
#         return num
#     num += 1
#     print(num)
#     recursion(num)
#
# recursion(1)


def sum_num(num):
    if num == 1:
        return  1

    temp = sum_num(num - 1)
    return temp + num


s = sum_num(3)
print(s)

