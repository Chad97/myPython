"""
根据约定 py中类的定义 首字母大写
这个类的定义空格是空的，因为要从空白创建这个类
"""


class Dog():
    """小狗的类"""

    def __init__(self, name, age):
        """初始化name和age属性"""
        self.name = name
        self.age = age

    def sit(self):
        """小狗坐下"""
        print(self.name.title() + "坐下~~汪汪汪")

    def roll(self):
        """小狗打滚"""
        print(self.name.title() + "打滚~ 汪汪汪")

    def say_hi(self):
        print('我的名字叫：%s 我几年%s岁' % (self.name, str(self.age)))


#  实例化对象
my_dog0 = Dog('apple', 6)
#  访问实例化类属性
print('my dog name is %s' % my_dog0.name.title())
#  实例化的方法
my_dog0.sit()
my_dog0.roll()
my_dog0.say_hi()

my_dog01 = Dog('旺财', 8)
my_dog01.say_hi()

"""
动手试一试
9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
9-3 用户 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User 中定义一个名
为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
"""


class Restaurant():
    """餐馆"""
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("我们餐厅叫 %s 是一家 %s厅 ,味道非常好" %(self.name, self.type))

    def open_restaurant(self):
        print('餐厅正在营业')


restaurant = Restaurant('好运来', '川菜')

restaurant.describe_restaurant()

restaurant2 = Restaurant('供你蒋', '粤菜')
restaurant3 = Restaurant('阿萨德', '港式')


class User():
    """描述用户"""
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def say_hi(self):
        """打招呼"""
        print('你好我的名字叫%s,很高兴认识你' % (self.first_name + self.last_name))


xiaomi = User('王', '小米')
xiaomi.say_hi()


class Car():

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def car_info(self):
        print('%s %s %s 行驶里程：%s' %(self.make, self.model, self.year, self.odometer_reading))

    #  通过方法修改属性
    def update_odometer(self, odometer):
        if float(odometer) > self.odometer_reading:
            self.odometer_reading = odometer
        else:
            print('禁止回调里程表')


my_car = Car('Audi', 'A8', '2020')
#  直接修改属性
my_car.odometer_reading = 66
my_car.car_info()
my_car.update_odometer(1)
my_car.car_info()

my_car2 = Car('Benz', 'GLA', '2019')


def say():
    print(123132)