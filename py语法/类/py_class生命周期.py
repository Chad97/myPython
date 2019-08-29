class Cat:
    #  类实例化时自动调用这个函数
    def __init__(self, name):
        self.name = name
        print('%s他来了 他来了' % self.name)

    #  对象被内存中销毁前，会被自动调用
    def __del__(self):
        print('他走了 他走了')

    #  类的实例打印时调用这个函数(返回)用户看到的
    def __str__(self):
        return '我是Cat的类'

    #  和上面的str函数一样,只是这个时返回开发者看到的
    def __repr__(self):
        return '__repr__'

    #  当调用不存在的属性时访问这个方法
    def __getattr__(self, item):
        item = 'A'
        print('属性不存在，默认为 %s' % item)

    #  如果类实现了这个方法，相当于把这个类型的对象当作函数来使用，相当于 重载了括号运算符
    def __call__(self, *args, **kwargs):
        print('我是 %s 通过__call__转函数实例化的' % args)


#  Tom 是一个全局变量
tom = Cat('Tom')
print(tom.name)
# del tom
print('-' * 50)
print(tom)
tom.sex
print('*' * 50)
tom('Tim')

