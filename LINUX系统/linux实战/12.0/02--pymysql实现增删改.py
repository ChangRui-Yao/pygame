"""
#1导入模块
#2创建连接对象
#3创建游标队形
#4使用游标对象执行SQL
#5提交
#6获取执行结果（影响的行数）并打印
#7关闭游标
#8关闭连接
"""
#1导入模块
import pymysql
#2创建连接对象
conn = pymysql.connect(host="localhost",user="root",password="123456",database="python_test_1")
#3创建游标对象
cur = conn.cursor()
#4使用游标对象执行SQL
#sql = 'insert into students values(null,"孙悟空",18,180,"男",1,0)'
#sql = 'delete from students  where id = 19'
sql = 'update students set name = "李元芳" where id = 17'
ret = cur.execute(sql)
#5提交
#提交刚刚执行的SQL
conn.commit()
#6获取执行结果（影响的行数）并打印
print("影响行数",ret)
#8关闭游标
cur.close()
#9关闭连
conn.close()