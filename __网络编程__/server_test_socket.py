import socket   #导入socket模块
s = socket.socket() #创建socket对象
host = socket.gethostname()  #获取本地ip地址
port = 12345   #设置端口
s.bind((host,port))   #绑定端口
s.listen(5)  #等待客户端连接
while True:
	c,addr = s.accept()  #建立客户端连接
	print('欢迎进入',addr)
	c.send('欢迎访问菜鸟教程!'.encode())
	c.close()    #关闭连接