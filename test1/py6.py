# -*- coding = utf-8 -*- 
import sqlite3

# 1、连接数据库
# 打开或创建数据库文件
conn = sqlite3.connect("test.db")

print("Open database successfully")

# 获取游标
c = conn.cursor()
# 2、创建数据表
sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real)
'''

# 3、插入数据
sql1 = '''
    insert into company (id, name, age, address, salary)
    values (1, "liz", 18, "bj", 19999)
'''
sql2 = '''
    insert into company (id, name, age, address, salary)
    values (2, "nany", 15, "sy", 1000)
'''

# 4、查询数据
sql4 = "select id, name, age, address, salary from company"

# 执行SQL语句
c.execute(sql)
c.execute(sql1)
c.execute(sql2)
cursor = c.execute(sql4)
for row in cursor:
    print("id: ", row[0])
    print("name: ", row[1])
    print("age: ", row[2])
    print("address: ", row[3])
    print("salary: ", row[4],"\n")
# 提交数据库操作
conn.commit()
# 关闭数据库连接
conn.close()

print("over")