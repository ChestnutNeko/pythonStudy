# # 输出
# print("hello python")
# # 输入
# name = input("please enter your name:")
# print("name:", name)

# a = 2
# if a > 0: 
#     print(a)
# else:
#     print(-a)

# # r''表示转义字符不转义
# print(r"///demo")
# # '''...'''表示多行内容
# print('''lizi
# 是
# 小可爱''')

# # 布尔值判断
# print(5 > 3)

# # 除法
# print("/", 10/3)
# # 地板除，取整
# print("//", 10//3)
# # 取余
# print("%", 10%3)

# print("1000 0.06 x 1", 1000/0.06)

# print("abcde的长度", len('abcde'))

# print("hello, %s" %"world")

# s1 = 72
# s2 = 85
# r = (s2-s1)/s1*100
# print('%.2f%%' % r)

# print('%.2f%%' % 24.2455)

# food = ["apple", "orange", "sweets"]
# # print("list的长度", len(food))
# # print("list第一个、第二个、倒数第一个元素", food[0], food[1], food[-1])
# # 末尾插入元素 append()
# food.append("banana")
# print(food)
# # 指定位置插入元素 insert()
# food.insert(2, "bread")
# print(food)
# # 删除末尾元素
# print(food.pop())
# print(food)
# # 删除指定位置元素
# print(food.pop(1))
# print(food)
# # 元素替换
# food[0] = "peach"
# print(food)

# tuple 没有append()，insert()
people = ("Liz", "Andy", "Bob")
print(people)
test = ("Jim")
print(test)
test2 = ("Jim", )
print(test2)