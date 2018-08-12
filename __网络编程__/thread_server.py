from socket import *
from threading import *
import sys
HOST = '0.0.0.0'
POST = 8888
ADDR = (HOST,PORT)

#创建套接字
s = socket()
s.bind(ADDR)
s.listen(5)

def handler(connfd):
	print('Got connection from',connfd.getpeername())
	while True:
		data = connfd.recv(1024).decode()
		if not data:
			break
		connfd.send(b'receive your message')
	connfd.close()

while True:
	try:
		connfd,addr = s.accept()
	except KeyboardInterrupt:
		sys.exit('服务器退出')
	except Exception as e:
		print(e)
		continue
	t = Thread(target = handler,args = (connfd,))
	t.setDaemon(True)
	t.start()
t.join()