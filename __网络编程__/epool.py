
from socket import *
from select import *
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)
#创建EPOLL对象
p = epoll()
#建立通过fileno查找IO对象的字典
fdmap = {s.fileno():s}
#注册关注IO事件
p.register(s,EPOLLIN | EPOLLERR)
while True:
    '''监控关注的IO'''
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('连接来自：',addr)
            #注册新的关注IO
            p.register(c,EPOLLIN | EPOLLERR)
            #维护字典
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:

        #else:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print(data.decode())
                fdmap[fd].send('收到了'.encode())
