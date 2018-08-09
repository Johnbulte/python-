from pymysql import *
class Mysqlpython:
    def __init__(self,user,passwd,db,host="localhost",port=3306,charset="utf8"):
        self.user = user
        self.passwd = passwd
        self.db = db
        self.host = host
        self.port = port
        self.charset = charset
    def open(self):
        self.conn = connect(user=self.user,passwd=self.passwd,db=self.db,host=self.host,port=self.port,charset=self.charset)
        self.cursor = self.conn.cursor()
    def close(self):
        self.cursor.close()
        self.conn.close()
    def zhixing(self,sql):
        self.open()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print('ok')
        except Exception as e:
            self.conn.rollback()
            print('Failed',e)
        self.close()



A=Mysqlpython('root','123456','MOUSHOU')
A.open()
