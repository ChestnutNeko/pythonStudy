# 正则表达式
import re
# 创建模式对象
pat = re.compile("AA") # 正则表达式
# m = pat.search("CBA") # search 被校验的
m = pat.search("CBAABDAA")
print(m)

r = re.search("po","adfpo")
print(r)

print(re.findall("[A-Z]+","AERsfFSswREdQf"))

print(re.sub("a","A","aade"))

# 建议在被比较的字符前加r，不用担心转义字符的问题
a = r"\aabd-\'"
print(a)