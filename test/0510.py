# 🍓vscode yyds

# 获取对象信息
# 判断对象类型 type()
print(type(123))
# <class 'int'>
print(type('123'))
# <class 'str'>
print(type(None))
# <class 'NoneType'>
print(type(abs))
# <class 'builtin_function_or_method'>
print(type(123) == int)
# True
# 判断函数
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
# True
# 🍇
# 基本数据类型 int str
# 继承关系 isinstance()判断
class Animals(object):
    def run(self):
        print('rrr')
a = Animals()
print(isinstance(a, Animals))
# True
print(isinstance('o', str))
# True
# 判断一个变量是否是某些类型中的一项
print(isinstance([1, 2, 3], (list, tuple)))
# True
print(isinstance((1, 2, 3), (list, tuple)))
# True

# 🍌获取一个对象所有属性和方法，dir() 返回一个包含字符串的list
# print(dir('ABC'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# __len__ 等价于 len()
print(len('123'))
# 3
print('123'.__len__())
# 3
print('ABC'.lower())
# abc
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
# hasattr() 有属性 setattr() 设置属性 getattr() 获取属性
print(hasattr(obj, 'x'))
# True
print(hasattr(obj, 'y'))
# False
print(setattr(obj, 'y', 122))
print(hasattr(obj, 'y'))
# True
print(getattr(obj, 'y'))
# 122
print(obj.y)
# 122
print(getattr(obj, 'z', 404)) # 无z返回404
# 404
print(getattr(obj, 'power')())
# 81
print(obj.power())
# 81

sum = obj.x + obj.y
print(sum)
# 131