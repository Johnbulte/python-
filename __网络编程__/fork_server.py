
from socket import *
import os,sys
import signal

# 地址
HOST = "0.0.0.0"
PORT = 8080
ADDR = (HOST,PORT)

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)


# 处理客户端请求函数
def client_handler(c):
	try:
		print("子进程接收客户端请求",c.getpeername())
		while True:
			data = c.recv(1024).decode()
			if not data:
				break
			print(data)
			c.send(b'Receive your message')
	except (KeyboardInterrupt,SystemExit):
		sys.exit(0)
	except Exception as e:
		print(e)
	c.close()
	# 结束子进程
	sys.exit(0)

print("父进程 %d 等待客服端连接请求"%os.getpid())
# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while True:
	try:
		c,addr = s.accept()
	except KeyboardInterrupt:
		sys.exit("服务器退出")
	except Exception as e:
		print(e)
		continue
	
	# 创建子进程
	pid = os.fork()
	if pid < 0:
		print("创建子进程失败")
		c.close()
		continue
	elif pid == 0:
		# 防止子进程操作s
		s.close()
		# 处理客户端请求
		client_handler(c)
	else:
		# 防止父进程操作c
		c.close()
		continue
