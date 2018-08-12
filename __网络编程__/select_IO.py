from socket import *
from select import select
import sys
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)
rlist = [s]
wlist = []
xlist = []
#r,w,x = select(rlist,wlist,xlist)
#c,addr = r[0].accept()
#print('连接来自',addr)
while True:
    print('等待连接.....')
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            connfd,addr = r.accept()
            print('连接来自：',addr)
            #增加关注事件
            rlist.append(connfd)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
            else:
                print('Receive:',data)
                #加入到要处理的IO事件
                wlist.append(r)
                #r.send(b"Receive your message")


    for w in ws:
        w.send('这是一条回复信息:'.encode())
        wlist.remove(w)
#处理发生异常的IO
    for x in xs:
        if x is s:
            s.close()
            sys.exit(0)

    #c,addr=r[0].accept()
    #print('连接来自：',addr)
