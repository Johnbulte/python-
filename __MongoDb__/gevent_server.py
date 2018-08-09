import gevent
#需要在引入socket之前调用
from gevent import monkey
monkey.patch_all()
from socket import *
from time import ctime
def server(port):
    s = socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print('Connect from ',addr)
        handler(c)
#处理客户端请求
def handler(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print('recv',data)
        c.send(ctime().encode())
    c.close()
server(8080)