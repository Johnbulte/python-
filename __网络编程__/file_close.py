from socket import *
s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)
c,addr = s.accept()
print('connect from',addr)
f = open('file.jpg','wb')
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)
data = c.recv(1024)
print(data.decode()
f.close()
c.close()
s.close()
