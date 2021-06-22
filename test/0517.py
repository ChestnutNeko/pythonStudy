# __str__()返回用户看到的字符串，__repr__()返回程序开发者看到的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Student object (name: %s)" % self.name
    __repr__ = __str__
print(Student('Liz'))
# __iter__()，类想被用于list或tuple
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
# __getitem__像list按下标取元素
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib2()
print(f[5])
# __getattr__()，没有属性时调用
class Stu2(object):
    def __init__(self):
        self.name = 'Liz'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
s = Stu2()
print(s.name)
print(s.score)
# 写SDK，链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list) 
# __call__()，直接对实例进行调用
class Stu3(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s' % self.name)
s3 = Stu3('Liz')
s3()
# 判断一个变量是对象还是函数，判断能否被调用
print(callable(max))
print(callable([1, 2, 3]))
print(callable(Stu3('liz')))

# 枚举类 Enum
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'APr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
@unique #检测有无重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
print(day1, day1.value)

@unique
class Gender(Enum):
    Male = 0
    Female = 1
# gender = Enum('Gender', ({'Male': '0', 'Female': '1'}))
class Stu4(object):
    def __init__(self, name, Gender):
        self.name = name
        self.gender = Gender
# 元类 type() 
# type()函数创建class类
# 先定义metaclass，就可以创建类，最后创建实例 
class ListMEtaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMEtaclass):
    pass
# try
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')