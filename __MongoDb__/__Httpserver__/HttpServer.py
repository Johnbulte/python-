#coding=utf-8 

'''
name : Levi
time : 2018-7-30
功能  : httpserve部分
'''

from socket import * 
import sys 
import re 
from threading import Thread 
from setting import *

#处理HTTP请求
class HTTPServer(object):
    def __init__(self,app):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.app = app

    def bind(self,addr):
        self.ip = addr[0]
        self.port = addr[1]
        self.sockfd.bind(addr)
    #启动http服务器    
    def serve_forever(self):
        self.sockfd.listen(10)
        print("Listen the port %d...."%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print("Connect from",addr)
            handle_client = Thread\
            (target = self.handle_client,args = (connfd,))
            handle_client.setDaemon(True)
            handle_client.start()

    def handle_client(self,connfd):
        #接受浏览器request
        request = connfd.recv(4096)
        request_lines = request.splitlines()
        #获取请求行
        request_line = request_lines[0].decode('utf-8')
        
        #获取请求方法和请求内容
        method,filename = \
        re.findall(r'^(\w+)\s+(/\S*)',request_line)[0]

        #将解析内容形成字典给Frame使用
        env = {'METHOD':method,"PATH_INFO":filename}

        #将请求内容给webframe的app应用
        #得到app处理请求后反馈的内容
        response = self.app(env)

        #发送给客户端
        if response:
            connfd.send(response.encode())
            connfd.close()


if __name__ == "__main__":

    #将setting配置中的MODULE导入到本地
    sys.path.insert(1,MODULE_PATH)
    m = __import__(MODULE)
    application = getattr(m,APP)

    httpd = HTTPServer(application)
    httpd.bind(ADDR)
    httpd.serve_forever()
