# -*- coding:utf-8 -*-
import traceback
import math


class Person(object):
    def __init__(self, name='李四', age=1):
        self.name = name
        self.age = age


p1 = Person()
p1.name = '张三'
print(p1.name)

p11 = Person('小红')
p12 = Person('小花')
print(p11.name, p11.age)
print(p12.name, p12.age)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


pp1 = Point(2, 3)
pp2 = Point(5, 7)
print(pp1.distance(pp2))


# 对象属性的增删改查
# 注意对象属性的增删改查都是针对指定的哪一个对象不会影响到其他对象
class Dog(object):
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type


dog1 = Dog('旺财', '黄色', '二哈')
# 查 getattr
# 当属性不存在时会报错
print(dog1.name)
print(getattr(dog1, 'color'))
print(getattr(dog1, 'type', '才才'))
# getattr(对象,属性名,默认值)当属性不存在的时候如果设置了默认值程序不崩溃而是返回默认值
print(getattr(dog1, 'sex', '公'))

# 改 setattr
# 修改
dog1.name = '大黄'
# 添加
dog1.address = 'cd'
print(dog1.address)

# 修改
setattr(dog1, 'name', '热狗')
# 添加
setattr(dog1, 'name2', '肉狗')

# 删除 del delattr
try:
    del dog1.name
    print(dog1.name)

    delattr(dog1, 'color')
    print(dog1.color)
except AttributeError:
    # 日志打印
    traceback.print_exc(file=open('error.txt', 'a+', encoding='utf-8'))
    print('没有这个属性')


class Student(object):
    number = 61
    # slots是用来约束当前这个类有哪些属性
    __slots__ = ('name', 'study_id', 'age', 'sex')

    def __init__(self, name, age):
        self.name = name
        self.study_id = '001'
        self.age = age


# 类的字段和内置类属性
'''
1.直接声明在类里面，函数的外面的变量就是类的字段
2.类的字段需要通过类来使用：类.字段
3.不会因为对象不同而不一样的数据就声明成类的字段
'''
print(Student.number)


class Dog1(object):
    """说明文档：狗类"""
    # 类的字段
    type = '犬科'

    # __slots__ = ('name', 'age', 'color')

    # 对象的属性
    def __init__(self, name='狗', age=5, color='白'):
        self.name = name
        self.age = age
        self.color = color

    # 对象方法
    def eat(self, food):
        print('%s在吃%s' % (self.name, food))

    # 类方法
    @classmethod
    def shout(cls):
        print('wangwang...')

    # 静态方法
    @staticmethod
    def bite():
        print('狗咬人')


dog1 = Dog1('小黑', 3, '黑色')
# __name__获取类的名字
print(Dog1.__name__)
# __class__获取对象对应的类
print(dog1.__class__)

aa = dog1.__class__
d1 = Dog1()
d2 = aa()
print(d1, d2)
print(Dog1.type)
print(aa.type)
print(dog1.__class__.__name__)

# __dict__用来获取当前类的所有类的字段及其对应的值
# 类.__dict__获取当前类的所有类的字段及其对应的值
print(Dog1.__dict__)
# 对象.__dict__当前对象所有的对象属性及其值转换成字典,key是属性名value是属性值。对象调用将对象的属性及其值转换成字典
print(dog1.__dict__)
# 如果给类的slots赋了值那么这个类的对象的dict属性就不能用了

# __bases__ 获取当前类的父类
# 类.__bases__
print(Dog1.__bases__)

# __module__(类.__module__获取当前类所在的模块的模块名
print(Dog1.__module__)

# __doc__(类.__doc__获取类的说明文档
print(Dog1.__doc__)


# 练习
# 1.声明一个电脑类：属性：品牌、颜色、内存大小 方法：打游戏、写代码、看视频
class Computer(object):
    def __init__(self, brand='华硕', color='黑色', memory='750G'):
        self.brand = brand
        self.color = color
        self.memory = memory

    def game(self):
        print('打游戏')

    def code(self):
        print('写代码')

    def video(self):
        print('看视频')


# 创建电脑类的对象，然后通过对象点的方式获取、修改、添加和删除它的属性
com1 = Computer()
print(com1.brand)
print(com1.color)
print(com1.memory)

com1.size = '15英寸'
print(com1.size)

try:
    del com1.size
    print(com1.size)
except AttributeError:
    print('属性不存在')

try:
    print(getattr(com1, 'color', '无该属性'))
    setattr(com1, 'color', '银灰色')
    print(getattr(com1, 'color'))
    delattr(com1, 'bluetooth')
    print(getattr(com1, 'bluetooth'))
except AttributeError:
    print('属性不存在')


class Circle(object):
    a = math.pi

    def __init__(self, r):
        self.r = r

    def area(self):
        return Circle.a * self.r ** 2

    def per(self):
        return 2 * Circle.a * self.r


circle1 = Circle(5)
print(circle1.area())


class Student1(object):
    def __init__(self, name, age, stuid):
        self.name = name
        self.age = age
        self.stuid = stuid

    def method(self):
        print(self.name, self.age, self.stuid)
        print('到')


student = Student1('小明', 20, '1201')
student.method()


# 类的方法和静态方法
# 类中的方法分为对象方法、类方法、静态方法
# 对象方法（1、直接声明在类中2、有默认参数self3、通过对象去调用）
# 类方法（1、在声明前添加@classmethod2、有默认参数cls调用的时候不需要给cls传参系统会自动调用当前类方法的类传给cls,cls最终指向的是一个类，类可以做的事cls都可以做3、通过类去调用：类.类方法（）
# 静态方法（1、在声明前添加@staticmethod2、没有默认参数3、通过类去调用：类.静态方法（）


# 对象方法、类方法、静态方法的选择
# 对象方法：当实现函数功能需要用到对象的属性的时候就使用对象方法
# 类方法:当实现函数的功能不需要对象属性但需要类的字段或创建对象等的时候就是用类方法
# 静态方法:实现函数的功能既不需要对象的属性也不需要类的时候就是用静态方法
class Math(object):
    pi = math.pi

    @staticmethod
    def my_sum(num1, num2):
        return num1 + num2

    @classmethod
    def circle(cls, r):
        return cls.pi * r ** 2

    @classmethod
    def destroy(cls):
        return Math.pi


print(Math.my_sum(2, 3))
print(Math.circle(2))
print(Math.destroy())


# 私有化
# 在类中可以通过在属性或方法名前加__,那么这个属性就会变成私有的；私有的属性和方法在类的外部不能使用
class Person2(object):
    __num = 200

    def __init__(self):
        self.name = '张三'

    def show(self):
        self.__show_message()

    def __show_message(self):
        print(Person2.__num)
        print('名字：', self.name)


print(Person2().show())


# 对象属性的getter和setter
# 如果希望在获取对象属性之前要做点儿别的事情,就给这个属性添加getter
# 如果希望在给对象属性赋值之前做点儿别的事情,就给这个属性添加setter
class Person3(object):
    def __init__(self, name='小红'):
        self.name = name
        self._age = 0
        self.sex = '男'

    @property
    def age(self):
        if self._age < 1:
            return '婴儿'
        elif self._age < 18:
            return '未成年'
        elif self._age < 50:
            return '中年'
        else:
            return '老年'

    @age.setter
    def age(self, value):
        # isinstance函数来判断一个对象是否是一个已知的类型，类似于type()
        # isinstance和type区别：type不会认为子类是一种父类类型不会考虑继承关系；isinstance会认为子类是一种父类类型考虑继承关系
        if not isinstance(value, int):
            print('年龄必须是整数')
            raise ValueError
        if not 0 < value <= 100:
            print('年龄超出范围')
            raise ValueError
        self._age = value


# __repr__
class Student3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return str(self.__dict__)[1:-1]


stu1 = Student3('小明', 29)
stu2 = Student3('小花', 18)
print(stu1, stu2)


# 类的继承
# 继承:1、python支持多继承2、python中默认情况是继承自object，object是所有类的基类
# 一个类可以继承另外一个类，继承者我们叫子类，被继承者我们叫父类，继承就是让子类拥有父类中的内容
# 所有的属性和方法都可以继承除了__clots__魔法对应的值不会被继承
# 子类中添加新方法父类不可以调用
# 重写父类方法：重新实现父类的方法 super()调用父类的方法再添加新功能
# 子类的方法中通过super()去调用父类的方法,super(类，对象）获取对象中父类的部分
# 静态方法中不能使用super()
# 类中方法的调用过程
# 1、通过对象或类调用方法的时候先看当前类中是否声明过这个方法如果生命过就直接调用当前类对应的方法
# 2、如果当前类中没有生命过就会去父类中有没有声明过这个方法声明过就调用父类方法
# 3、如果父类也没有声明过就去找父类的父类以此类推直到object中也没有声明过程序才会崩溃

# 添加属性
# 1、添加类的字段：直接在子类中添加新的字段
# 2、添加对象属性：类的对象属性是通过继承父类init方法继承下来的如果想要保留父类继承下来的对象属性前提下添加新的对象属性需要在子类init方法中
# 通过super()去调用父类的init方法
class Animal(object):
    sex = '公猫'

    def __init__(self, color, ty, age=1):
        self.color = color
        self.type = ty
        self.age = age


class Cat(Animal):
    def __init__(self, color, age=5, hobby='鱼'):
        super().__init__(color, '猫科', age)
        self.hobby = hobby
        self.music = '喵喵喵'


cat1 = Cat('白色')
print(cat1.type, cat1.hobby, cat1.age, cat1.color, cat1.music, Cat.sex)


# init,call,new及del方法的使用
# init主要是创建对象时进行初始化操作会自动调用
# new方法是类准备将自身实例化时调用，是一个静态方法new(cls,*args,**kwargs):
# cls时当前正在实例化的类、*args,**kwargs是实例化传入的参数,new方法在实例化开始之后,init方法调用之前调用
# call方法能够让类的实例对象像函数一样调用
# del析构方法，是python的垃圾回收实际应用，当类的所有引用都被删除后该类就会被系统从内存中删除

class Student5(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('创建对象成功')

    def __new__(cls, *args, **kwargs):
        print('new方法')
        return super(Student5, cls).__new__(cls)

    def __call__(self, na):
        print('调用call方法', '姓名%s' % na)

    def __del__(self):
        print('对象已经删除')


stu = Student5('鲁班', 18)('李白')

stu1 = Student5('鲁班', 18)


# 单下划线和双下划线属性的区别
# 单下划线开始的成员变量叫做保护变量意思是只有类对象和子类对象自己能访问到这些变量
# 双下划线开始的是私有成员意思是只有类对象自己能访问连子类对象也不能访问到这个变量
class Foo(object):
    def __init__(self):
        pass

    def public_method(self):
        print('这是一个公开的方法')
        self.__fullprivate_method()

    def __fullprivate_method(self):
        print('这是一个私有方法')

    def _halfprivate_method(self):
        print('这是一个受保护的方法')


f = Foo()
f.public_method()
f._halfprivate_method()


# 面向对象和pygame
# 多继承
# 1、多继承：让一个类同时继承多个类
# 2、多态:一个事物的多种形态；一个类实例的相同方法在不同情况下有不同的表现形式
class Animal1(object):
    pass


class Dog1(Animal1):
    pass


class Cat1(Animal1):
    pass


# isinstance():判断一个对象是否属于某种类型
a = []
b = Animal1()
c = Cat1()
print(isinstance(a, list))
print(isinstance(b, Animal1))  # True
print(isinstance(b, Dog1))  # False
print(isinstance(c, Cat1))


# 运算符重载
# 运算符重载：python中运算符实质就是在调用相应的魔术方法；在不同的类中实现同一个运算符对应的魔术方法

class Student6(object):
    def __init__(self, name='', score=0, age=0):
        self.name = name
        self.score = score
        self.age = age

    def __add__(self, other):
        return self.score + other.score

    def __sub__(self, other):
        return self.score - other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score


stu6 = Student6('张三', 100, 32)
stu7 = Student6('李四', 90, 25)

print(stu6 + stu7)


# 多态练习
class Person6(object):
    def feedAnimal(self, ani):
        print("喂动物：", ani.name)
        ani.eat()


class Animal6(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating")


class Cat6(Animal6):
    def __init__(self, name):
        super(Cat6, self).__init__(name)


class Dog6(Animal6):
    def __init__(self, name):
        super(Dog6, self).__init__(name)


p = Person6()
c = Cat6("小白")
p.feedAnimal(c)

d = Dog6("旺财")
p.feedAnimal(d)


# 单例模式
class Person7(object):
    instance = None

    init_flag = False

    def __init__(self):
        if Person7.init_flag:
            return
        print('进行初始化操作')
        Person7.init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


person1 = Person7()
person2 = Person7()
