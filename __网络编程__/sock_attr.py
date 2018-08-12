#sock_attr.py
from socket import *
s = socket()
#获取套接字类型
print(s.type)
#获取地址族类型
print(s.family)
#获取文件描述符
print(s.fileno())
s.setsockopt(SQL_SOCKET,SO_REUSEADDR,1)#取消断网保护机制
s.bind(('127.0.0.1',8888))
#获取套接字的绑定地址
print(s.getsockname())
s.listen(5)
c,addr = s.accept()
#获取连接段地址
print(s.getpeername())
