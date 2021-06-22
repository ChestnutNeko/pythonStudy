# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' %func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def fn():
#     print('xx')
# fn()

# print(int('124444445', 16))

# def int2(x, base=2):
#     return int(x, base)
# print(int2('111000'))

# import functools
# fun2 = functools.partial(int, base=2)
# print(fun2('10001'))

# 模块 Module
# 每个包下面都有一个__init__.py文件，将目录看成普通目录，__init__.py可为空
# python代码 -> 模块 -> 包