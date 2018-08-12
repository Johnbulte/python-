#超时检测机制
from socket import *
from time import sleep,ctime
s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
#设置s为非阻塞
#s.setblocking(False)
'''设置超时等待时间'''
s.settimeout(5)
while True:
    print('Wating for connect')
    try:
        connfd,addr = s.accept()
    except timeout:
        print('连接超时......')
        sleep(2)
        print(ctime())
        continue
    print('CONNECT from',addr)
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        connfd.sendall(ctime().encode())
    connfd.clsoe()
s.close()
