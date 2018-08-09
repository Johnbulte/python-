import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='MOSHOU',charset='utf8')
cur = db.cursor()
try:
    name = input('请输入省：')
    s_id = input('请输入该省的编号：')
    sql_insert = "insert into sheng(s_id,s_name) \ values(%s,%s)"
    cur.execute(sql_insert,[s_id,name])
    db.commit()
    print('ok')
except Exception as e:
    db.rollback()
    print('出现错误，已回滚')
cur.close()
db.close()
