
from bs4 import BeautifulSoup
import re

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# print(bs.a)
# 1、Tag 标签及其内容：拿到它所找到的第一个内容

# print(bs.title.string)
# print(type(bs.title.string))
# 2、NavigableString 标签里的内容（字符串）

# print(bs.a.attrs)
# bs.a.attrs 获取a标签里的所有属性，返回一个字典

# print(bs)
# 3、BeautifulSoup 表示整个文档

# print(bs.a.string)
# 4、输出的内容不包含注释符号

# --------------------------------

# 文档的遍历
# print(bs.head.contents)

# 文档的搜索
# (1)find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
# (2)t_list = bs.find_all("a")
# 正则表达式搜索：使用search()方法来匹配内容
# (3)t_list = bs.find_all(re.compile("a"))
# 方法：传入一个函数（方法）
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)
# print(t_list)

# 2、kwargs 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# 3、text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图"])
# t_list = bs.find_all(text=re.compile("\d"))

# 4、limit参数
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)

# css选择器
# t_list = bs.select("title") # 通过标签来查找
# t_list = bs.select(".mnav") # 按照类名来查找
# t_list= bs.select("#ul") # 按照id来查找
# t_list = bs.select("a[class='bri']") # 通过属性来查找
# t_list = bs.select("head > title") # 通过子标签查找
t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())
# for item in t_list:
#     print(item)