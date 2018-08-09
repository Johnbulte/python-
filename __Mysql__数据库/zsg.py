import pymysql

#1.创建数据库连接对象
conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='MOSHOU',charset='utf8')
#2创建游标对象
cur=conn.cursor()

#3.利用游标对象的execute方法执行sql语句
cur.execute("insert into sheng values(33,999999,'新疆');")
#4.提交到数据库执行
conn.commit()

#5.关闭游标
cur.close()
#6.关闭数据库连接
conn.close()
