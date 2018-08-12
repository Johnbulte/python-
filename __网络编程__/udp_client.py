# udp_client.py


from socket import *
import sys


if len(sys.argv) < 3:
    print('''
            argv is error!!
            run as
            python3 udp_client.py 127.0.0.1 8888
            ''')
    raise

HOST = sys.argv[1]
PORT = int(sys.argv[2])
server_addr = (HOST,PORT)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('消息:')
    if not data:
        break
    #给服务器发送
    sockfd.sendto(data.encode(),server_addr)

    #收到服务器回复
    data,addr = sockfd.recvfrom(1024)
    print('从服务器收到：',data.decode())

sockfd.close()
