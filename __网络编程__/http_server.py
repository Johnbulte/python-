#!/usr/bin/python3
from socket import *
#处理请求，返回响应
def handleClient(connfd):
    print('CONNECT from ',connfd.getpeername())
    request = connfd.recv(4096)
    #print(request)
    requestHeadlers = request.splitlines()
    for line in requestHeadlers:
        print(line)
    #无论什么请求给出相同的响应
    try:
        f = open('index.html')
    except IOError:
        response = "HTTP/1.1 404 not found\r\n"
        response += '\r\n'  #空行
        response += '===Sorry,The page not found==='
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'  #空行
        for i in f:
            response += i
    finally:
        connfd.send(response.encode())
    connfd.close()




#网络连接控制流程
def main():
    '''创建套接字'''
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(5)
    '''请求连接'''
    while True:
        print('listen to the port 8000...')
        connfd,addr = sockfd.accept()
        #处理具体的客户端请求
        handleClient(connfd)

if __name__ =="__main__":
    main()
