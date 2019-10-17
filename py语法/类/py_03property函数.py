# coding=utf-8
# Python property()函数：定义属性

""" 基本格式
属性名=property(fget=None, fset=None, fdel=None, doc=None)
开发者调用 property() 函数时，可以传入 0 个（既不能读，也不能写的属性）、1 个（只读属性）、2 个（读写属性）、3 个（读写属性，也可删除）和 4 个（读写属性，也可删除，包含文档说明）参数。
"""

class Rectangle:
    # 定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 定义setsize()函数
    def setsize(self, size):
        self.width, self.height = size

    # 定义getsize()函数
    def getsize(self):
        return self.width, self.height

    # 定义delsize()函数
    def delsize(self):
        self.width, self.height = 0, 0

    # 使用property定义属性
    size = property(getsize, setsize, delsize, '用于描述属性大小的属性')


# 访问size属性的数码文档
print(Rectangle.size.__doc__)

# 通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangle.size)

rect = Rectangle(6, 6)
# 对rect的size属性赋值
rect.size = 9, 7

# 访问rect的width、height实例变量
print(rect.width)  # 9
print(rect.height)  # 7

# 删除rect的size属性
del rect.size

# 访问rect的width、height实例变量
print(rect.width)  # 0
print(rect.height)  # 0


#  小栗子 读写
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return self.first.title() + " " + self.last

    def set_name(self, name):
        self.first, self.last = name

    # 定义property
    name = property(get_name, set_name)


# 访问实例
xm = User('tom', 'eric')
print(xm.name)

# 设置实例属性
xm.name = 'xiao', 'mi'
print(xm.name)
# 访问实例变量
print(xm.first, xm.last)
