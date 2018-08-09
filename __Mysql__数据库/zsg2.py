import pymysql

db=pymysql.connect(host="localhost",user="root",passwd="123456",db="MOSHOU",charset="utf8")
cur=db.cursor()

try:
    sql_delete="delete from sheng where id=1;"
    cur.execute(sql_delete)

    sql_update="update sheng set id=200 where id=2;"
    cur.execute(sql_update)

    db.commit()
    print('ok')
except Exception as e:
    db.rollback()
    print('Failed',e)

cur.close()
db.close()
