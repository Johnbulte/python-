from socket import *
from select import select
import sys
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)
#三个关注列表
rlist = [s,sys.stdin]
wlist = []
xlist = []
f = open('test.txt','w')
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin:
            data = r.readline()#获取从终端输入的内容
            f.write(data)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
            else:
                f.write(data.decode()+'\n')
