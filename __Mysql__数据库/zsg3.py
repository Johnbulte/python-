import pymysql

db=pymysql.connect(host="localhost",user="root",passwd="123456",db="MOSHOU",charset="utf8")
cur=db.cursor()
try:
    sql_select = "select * from sheng;"
    cur.execute(sql_select)   #所有查询结果都在cur对象里
    data = cur.fetchone()
    print(data)
    print('******************************************************************')
    data2 = cur.fetchmany(3)
    print(data2)
    print('******************************************************************')
    data3 = cur.fetchall()
    print(data3)
    print('******************************************************************')
    print('ok')
    db.commit()
except Exception as e:
    print(e)
cur.close()
db.close()
