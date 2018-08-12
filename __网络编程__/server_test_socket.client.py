import socket
s = socket.socket()   #创建socke模块
host = socket.gethostname()   #获取本地主机名
port = 12345
s.connect((host,port))
print(s.recv(1024).decode())
s.close()