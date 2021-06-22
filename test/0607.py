# -*- coding = utf-8 -*-
# import random
# num0 = int(input('你的输入为（剪刀（0），石头（1），布（2））：'))
# num1 = random.randint(0,2)
# print('随机生成数字为：%d' %num1)
# if num0 == num1:
#     print('平局哦')
# elif (num0 == 2 and num1 == 1) or (num0 == 1 and num1 == 0) or (num0 == 0 and num1 == 2) :
#     print('哈哈，你输了：）')
# else:
#     print('呜呜呜QAQ')

# # for...in...遍历字符串
# city = "chengdu"
# for i in city:
#     print(i)

# list = ["aa", "bb", "cc", "dd"]
# for i in range(len(list)):
#     print(i, list[i])


# 99乘法表
# for i in range(1,10):
#     print('\t')
#     for j in range(1, i+1):
#         print("%d*%d=%d" %(j, i, i*j), end='\t')

# 办公室分老师
# import random
# offices = [[],[],[]]
# teachers = ["a","b","c","d","e","f","g","h"]
# for i in teachers:
#     index = random.randint(0,2)
#     offices[index].append(i)
# print(offices)
# i = 1
# for j in offices:
#     print("办公室%d的人数为：%d"%(i,len(j)))
#     i += 1
#     for k in j:
#         print("%s"%k,end="\t")
#     print("\n")
#     print("-"*20)


# produces = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
# print("-"*5+"商品列表"+"-"*5)
# index = 0
# for i in produces:
#     print(index, produces[index][0], produces[index][1], "\t")
#     index += 1
# price = 0
# shopping = []
# carts = []
# order = input("购买请按y，退出请按q：")
# while order == "y":
#     num = int(input("请输入产品编码："))
#     shopping.append(produces[num][1])
#     carts.append(produces[num][0])
#     order = input("继续购买请按y，退出请按q：")
# for i in shopping:
#     price += i
#     if(i == shopping[-1]):
#         print("谢谢光临，购买了：%s，总价钱为：%d"%(carts,price))

# 打印n条横线
# def lines(n):
#     return n*("-------------""\n")
# print(lines(6))
# # 求三个数的和
# def sum(a, b, c):
#     return a+b+c
# print(sum(1, 2, 3))
# # 平均数
# def prov(a, b, c):
#     return sum(a, b, c)/3
# print(prov(2, 3, 4))

# f = open("ppp.txt", "r")
# # f.write("hello world")
# content = f.readlines()
# i = 0
# for a in content:
#     print(i,":",a)
#     i += 1
# f.close()
# 
f1 = open("gushi.txt", "w")
f1.write("《咏鹅》""\n""鹅鹅鹅，""\n""曲项向天歌，""\n""白毛浮绿水，""\n""红掌拨清波。")
# def readTxt(file):
#     pass
# f2 = open("copy.txt", "r")
# print("复制完毕")
f1.close()

def writeFile(filename,content):
    f = open(filename,"w")
    for i in content:
        f.write(i)
    f.close()

def readFile(filename):
    f = open(filename,"r")
    contents = f.readlines()
    return contents
    f.close()

gushi = ["日照香炉生紫烟\n,遥看瀑布挂前川\n,飞流直下三千尺\n,疑似银河落九天\n"]
writeFile("gushi.txt",gushi)
contents = readFile("gushi.txt")
copy = []
for content in contents:
    copy.append(content)
writeFile("copy.txt",copy)
# 