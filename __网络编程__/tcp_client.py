#tcp_client.py 
from socket import * 

#创建套接字 tcp 默认参数即可 
sockfd = socket()

#发起链接请求
sockfd.connect(('127.0.0.1',8888))

while True:
    data = input("发送>>")

    if not data:
        break 

    #发送消息 bytes格式
    sockfd.send(data.encode())

    data = sockfd.recv(1024).decode()
    print(data)

#关闭套接字
sockfd.close()