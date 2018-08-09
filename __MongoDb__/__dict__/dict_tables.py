#导入数据库模块
import pymysql
import re

f = open('dict.txt')
db = pymysql.connect\
('localhost','root','123456','dict')  #创建数据库连接
cursor = db.cursor()  #生成游标

for line in f:
	l = re.split('[ ]+',line)
	word = l[0]
	interpret = ''.join(l[1:])
	sql = "insert into words (word,interpret) values ('%s','%s')"\
	%(word,interpret)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
f.close()