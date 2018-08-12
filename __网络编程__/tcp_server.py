#tcp_server.py
from socket import *

#创建tcp套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定IP和端口
sockfd.bind(("127.0.0.1",8888))

#设置监听
sockfd.listen(5)

while True:
    #等待客户端链接
    print("Waiting for connect....")
    connfd,addr = sockfd.accept()
    print("Connect from",addr)

    while True:
        #接收
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive message >>",data.decode())

        #发送
        n = connfd.send(b"Receive your message\n")
        print("Send %d bytes data"%n)
    #关闭套接字
    connfd.close()


sockfd.close()