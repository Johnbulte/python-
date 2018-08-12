from socketserver import *

#多进程tcp并发


#创建指定类型的服务器
class Server(ForkingMixIn,TCPServer):
	pass

#处理具体请求
class Handler(StreamRequestHandler):
	def handle(self):
		print('CONNECT from',\
			self.request.getpeername())
		while True:
			data = self.request.recv(1024).decode()
			if not data:
				break
			print(data)
			self.request.send(b'Receive your message')

#生成服务器对象
server = Server(('0.0.0.0',8888),Handler)

#启动服务器
server.serve_forever()