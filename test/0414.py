# # !/user/bin/env python3
# # -*- coding = utf-8 -*-
# 'a test module'
# __author__ = 'Liz'
# import sys
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print('Hello World')
#     elif len(args) == 2:
#         print('Hello, %s!' % args[0:])
#     else:
#         print('lalala')
# if __name__ == '__main__':
#     test()
# # python解释器将__name__，置为__main__
# print(__name__)

# # 作用域 abc公有函数，直接定义；__name__等，特殊变量，可以被直接引用；_abc、__ab，私有函数，不应该被直接引用
# def _abc(name):
#     print('Hello, %s!' % name)
# def callName():
#     return _abc('Liz')
# callName()

# 安装第三方库，包管理工具pip

# 面向对象的编程OOP，把对象作为基本单元，一个对象包含数据和操作数据的函数
# Class 定义类，类中第一个参数永远是self

# 面向过程的栗子
# stu1 = {'name': 'Liz', 'age': 14}
# stu2 = {'name': 'Nacy', 'age': 15}
# def info(stu):
#     print('%s:%s' %(stu['name'], stu['age']))
# info(stu2)
# 面向对象的栗子
# class Stu(object): # 从object继承的类
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def stu_info(self):
#         print('%s:%s' % (self.name, self.age))
# liz = Stu('Liz', 18)
# nan = Stu('Nancy', 23)
# liz.stu_info()
# nan.stu_info()
# print(liz.name)
# 数据封装，在class内部定义访问数据的函数，也就是类的方法
# 创建实例需要定义每个属性的实例

# 让内部属性不被外部访问，在属性名称前加__。
# self.__name = name
# class Stu(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#     def stu_info(self):
#         print('%s:%s' % (self.__name, self.age))
# liz = Stu('Liz', 18)
# nan = Stu('Nancy', 23)
# liz.stu_info()
# nan.stu_info()
# print(liz.__name)
# 确保了外部代码不能随意修改对象内部的状态，可以为Stu类加上get_name方法
    # ...
    # def get_name(self):
    #     return self.__name
# 允许外部代码修改
    # ...
    # def get_age(self, age):
    #     self.__age = age
# 对参数进行检查，避免传入无效参数
    # ...
    # def get_age(self, age):
    #     if 0 < age < 120:
    #         self.__age = age
    #     else:
    #         raise ValueError('bad age')
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#     def set_gender(self, gender):
#         if gender == 'male' or 'female':
#             self.__gender = gender
#         else:
#             raise ValueError('bad gender')

# 继承和多态
# 继承 子类获得了父类的全部功能
class Animals(object):
    def run(self):
        print('run run run')
class Dog(Animals):
    def run(self):
        print('wang wang wang')
dog = Dog()
dog.run()
class Cat(Animals):
    pass
cat = Cat()
cat.run()
# 子类父类存在相同的方法时，子类会覆盖父类的方法

# 多态
# 判断数据是否是某种类型 isinstance()
print(isinstance(cat, Cat))
print(isinstance(cat, Animals))
# 
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animals())
run_twice(Dog())

# 开闭原则，对扩展开放，允许新增Animal子类；对修改关闭，不需要修改依赖Animal类型的run_twice等函数
# react是一个声明式，高校且灵活的用于构建用户界面的js库。使用react可以将一些简短、独立的代码片段组合成复杂的UI界面，这些代码被称为组件
# 特点：声明式、组件化
