# def fn(x):
#     return x*x
# a = map(fn, [1, 2, 3])
# print(list(a))
# print(list(map(fn, [1, 2, 3, 4])))

# b = map(str, [1, 2, 3, 4])
# print(list(b))

# print(list(map(str, [1, 2, 3, 4])))

# reduce
# from functools import reduce
# def add(x, y):
#     return x + y
# print(reduce(add, [1, 2, 3, 4]))

# print(float("123.3423"))

# print(sorted([36, 5, -12, 9, -21], key=abs))

# 闭包
# def calc_sum(*args):
#     def sum():
#         n = 0
#         for i in args:
#             n = n + i
#         return n
#     return sum
# f = calc_sum(1, 2, 3, 4)
# print(f())

# def createCounter():
#     def inc():
#         i = 0
#         while True:
#             i = i + 1
#             yield i
#         return i
#     inc2 = inc()
#     def counter():
#         return next(inc2)
#     return counter
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# f = lambda x: x * x
# print(f)

# print(f(5))


# def fn():
#     print('fn呀')

    # return 1
# f = fn()
# print(f)

# fn()
# print(fn.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def fn():
    print('fn呀')
fn()