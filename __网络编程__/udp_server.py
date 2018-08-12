# udp_server.py


from socket import *
import sys

#从命令行传入ip和端口
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(ADDR)

while True:
    #接收消息
    data,addr = sockfd.recvfrom(1024)
    print("Receive from %s,%s" % (addr,data.decode()))

    #发送消息

    sockfd.sendto("收到你的消息".encode(),addr)

#关闭套接字
sockfd.close()
