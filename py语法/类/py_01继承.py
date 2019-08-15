from py_00创建类 import Car


class Battery():
    """实例作用属性"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('电量剩余：%s' % self.battery_size)

    def get_range(self):
        """打印电池续航"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 280

        message = "电池电量为 %.02f 续航 %.02f 公里" % (self.battery_size, range)

        print(message)


class ElectricCar(Car):
    """电动汽车的特殊之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        #  引出抽离的 类
        self.battery = Battery()

    #  重写 子类 info 函数（会覆盖父类的方法）
    def car_info(self):
        print("我是电动汽车：%s" % self.make.title())


my_tesla = ElectricCar('tesla', 'Model-X', 2019)

my_tesla.update_odometer(999)

my_tesla.car_info()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()