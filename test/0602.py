# 调试 print()
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
# def main():
#     foo('0')
# main()

# 断言 assert()
# def foo2(s):
#     n = int(s)
#     assert n != 0, 'n is zero'
#     return 10 / n
# def main2():
#     foo2('0')
# main2()

# logging
# import logging
# logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# pdb 启动Python调试器pdb，让程序以单步方式运行，可以随时查看运行状态
# s2 = '0'
# n2 = int(s2)
# print(10 / n2)

# pdb.set_trace()
# import pdb
# s3 = '0'
# n3 = int(s3)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n3)

# 单元测试
# TDD test driven development 测试驱动开发 单元测试
# 对一个模块、一个函数或者一个类来进行正确性检验的测试工作
abs(-1)
print(abs(-1))

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
d = Dict(a=1, b=2)
d['a']
print(d['b'])
# 安全性 兼容性 HarmonyOS Windows MacOS Android IOS
# C2M Customer to Manufacturer 反向指导生产
# 库存周转天数
# 商品供应链+物流供应链
# View Controller Model
# 合并同类项 Domain Model 领域模型 存到ORM层 App State Modal 应用状态模型 
# 视图层组件
# Rudex 单向数据流 
# 纯函数 function add(a, b) { return a + b; } 非纯函数 function now() { let now = new Date(); return now; }
# store 数据存放的地方，store保存从进入页面开始所有