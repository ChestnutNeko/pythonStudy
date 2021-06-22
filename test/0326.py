# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(3))
# 6
# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# print(fact(3))

# people = ["Andy", "Lily", "Popi", "Uu", "Wendy"]
# print(people[0:4:2])
# ['Andy', 'Popi']

# food = ("apple", "nuts", "banana", "strawberry", "chicken")
# print(food[:3])
# ('apple', 'nuts', 'banana')

# print("asdfghjkl"[::2])
# adgjl

# for i in 'qwertyuiop':
#     print(i)
# from collections.abc import Iterable
# print(isinstance('asdf', Iterable))

# 列表生成式
# 1-4
# print(list(range(1, 5)))

# 1*1-4*4
# print(list(i*i for i in range(1,5)))

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)

# g = (x * x for x in range(3))
# print(g)
# print(next(g))
# for i in g:
#     print(i)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# print(fib(6))

# def num():
#     print('111')
#     yield(1)
#     print('222')
#     yield(2)
# n = num()
# next(n)

def triangles():
    num = 0
    if num == 0:
        list = [1]
        num += 1
        yield list
    if num == 1:
        list = [1, 1]
        num += 1
        yield list
    if num>1:
        while True:
            list = [1] + [(list[i] + list[i+1]) for i in range(len(list)-1)] + [1]
            num += 1
            yield list
print(next(triangles()))