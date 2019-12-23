"""
#1目标插入十万条数据
#2导入模块
#创建连接对象
#创建游标对象
#for循环插入十万条数据
#提交
#关闭游标对象
#关闭连接对象
"""


#2导入模块
import pymysql
#创建连接对象

conn = pymysql.connect(host="localhost",user="root",password="123456",database="python_index_db")
#创建游标对象
cur = conn.cursor()
#for循环插入十万条数据
for i in range(100000):
    cur.execute("insert into test_index(title) value ('ha - %d')" % i)



#提交
conn.commit()
#关闭游标对象
cur.close()
#关闭连接对象
conn.close()


