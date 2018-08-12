from socketserver import *

#多进程udp并发

class Server(ForkingUDPServer):
	pass
class Handler(DatagramRequestHandler):
	def handle(self):
		#接收消息
		while True:
			data = self.rfile.readline().decode()
			if not data:
				break
			print(data)
			self.wfile.write(b'Receive message')
#生成服务器对象
server = Server(('0.0.0.0',8888),Handler)

#启动服务器
server.serve_forever()
		