# 条件判断
# height = 24
# if height > 30:
#     print("1")
# elif height > 5:
#     print("2")
# else:
#     print("3")

# for...in
# food = ["apple", "nut", "coke"]
# for item in food:
#     print(item)

# while
# n = 0
# while n < 5:
#     n = n + 1
#     if n%2 == 0:
#     	continue
#     print(n)

# info = {"name": "Liz", "age": "18", "weight": "44kg"}
# print(info["name"])
# info["height"] = "160cm"
# print(info)
# print(info.get("height"))
# print(info.pop("name"))
# print(info)

# s = set([1, 2, 3, 2])
# print(s)
# s.add(4)
# s.remove(1)
# print(s)
# a = set([1, 2, 5])
# print(a & s)
# print(a | s)

# print(abs(-10))

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-2))
# print(my_abs("2"))

# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5, 2))
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(5))
# 栗子Neko

# def calc(*numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum + x*x
#     return sum
# print(calc(1, 2, 3))

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# print(person("Liz", 18))

# extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(person('Jack', 24, **extra))

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
# Jack 24 Beijing Engineer