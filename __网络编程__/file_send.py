from socket import *
s = socket()
s.connect(('127.0.0.1',8888))
f = open('img.jpg','rb')
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)
s.send('发送完毕'.encode())
f.close()
s.close()
