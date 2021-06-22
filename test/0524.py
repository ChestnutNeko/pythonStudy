# try
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
# 错误也是class，错误类型继承自BaseException
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
# main()

# 调用栈
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')
# main()

# 记录错误 Python内置的logging模块
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

# 抛出错误
# Pyhton的内置函数会抛出很多类型的错误，我们自己编写的函数和也可以抛出错误。尽量用python自带的，ValueError\TypeError
# err_raise.py
class FooError(ValueError):
    pass
def foo2(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' %s)
    return 10 / n
foo2('0')

from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()