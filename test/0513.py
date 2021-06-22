# 实例属性和类属性
class Student(object):
    height = '180cm' # 类属性
    def __init__(self, name):
        self.name = name
s = Student('Liz')
s.score = 90 # 实例属性
print(s.height, s.score)

s2 = Student('Andy')
# print(s2.height, s2.score)

# 实例属性和类属性不要使用相同的名字，实例属性将屏蔽类属性的

class Student2(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student2.count += 1
ss = Student2('ann')
print(ss.count)
ss2 = Student2('www')
print(ss2.count)

# 面向对象的高级编程
# 限制实例的属性，只允许对Student实例添加name和age属性 __slots__
class Stu(object):
    __slots__ = ('name', 'age')
stu1 = Stu()
stu1.name = 'Frank'
stu1.age = 14
# stu1.height = 180
# print(stu1.age, stu1.name, stu1.height)

# 对子类不生效
class StuSon(Stu):
    pass
stu2 = StuSon()
stu2.height = 180
print(stu2.height)

# @property装饰器把一个方法变成属性调用 方法名称和实例变量名称不要重复（会造成无限递归）
class Stuu(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value
uu = Stuu()
uu.score = 80
print(uu.score)

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        if value < 0:
            raise ValueError('width must be greater than 0')
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer')
        if value < 0:
            raise ValueError('height must be greater than 0')
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

# 多重继承
class Animal(object):
    pass
# 大类
# 哺乳类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# 给动物加上Runnable和Flyable的功能
class RunnableMixIn(object):
    def run(self):
        print('run run run')
class FlyableMixIn(object):
    def fly(self):
        print('fly fly fly')
# 各种动物
# MixIn多重继承
class Dog(Mammal, RunnableMixIn):
    pass
class Bat(Mammal, FlyableMixIn):
    pass
class Parrot(Bird):
    pass
class Ostirch(Bird):
    pass