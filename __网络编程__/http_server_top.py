from socket import *  
from threading import Thread 
import time 

#存放静态页面
STATIC_DIR = './static'
ADDR = ('0.0.0.0',8000)

#httpserver类　封装服务器功能
class HTTPServer(object):
    def __init__(self,addr):
        #套接字创建
        self.sockfd = socket()
        self.sockfd.setsockopt\
        (SOL_SOCKET,SO_REUSEADDR,1) 
        self.sockfd.bind(addr)
        self.sockfd.listen(5)
        #为对象添加属性
        self.name = "HTTPServer"
        self.port = addr[1]
        self.address = addr 

    #　监听客户端链接请求，创建新的线程处理
    def serve_forever(self):
        print("Listen to port %d..."%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            #创建新的线程处理具体请求
            clientThread = Thread\
            (target = self.handleRequest,args = (connfd,))
            clientThread.setDaemon(True)
            clientThread.start()

    def handleRequest(self,connfd):
        #接受客户端请求
        request = connfd.recv(4096)
        #解析请求
        requestHeadlers = request.splitlines()
        #打印请求行
        print(connfd.getpeername(),':',\
            requestHeadlers[0])

        #获取具体请求内容
        getRequest = \
        str(requestHeadlers[0]).split(' ')[1]

        if getRequest == '/' or getRequest[-5:] == ".html":
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)        
        connfd.close()

    def get_html(self,connfd,page):
        if page == '/':
            getFilename = STATIC_DIR + "/index.html"
        else:
            getFilename = STATIC_DIR + page
        
        try:
            f = open(getFilename)
        except Exception:
            #没有找到页面
            responseHeaders = "HTTP/1.1 404 not found\r\n"
            responseHeaders += "\r\n"
            responseBody = "===Sorry,the page not found==="
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n" 
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self,connfd,data):
        responseHeaders = 'HTTP/1.1 200 OK\r\n'
        responseHeaders += '\r\n'

        if data == "/time":
            responseBody = time.ctime()
        elif data == "/tedu":
            responseBody = "1234567"
        else:
            responseBody = "the data not found"

        response = responseHeaders + responseBody
        connfd.send(response.encode())



if __name__ == "__main__":
    #生成对象
    httpd = HTTPServer(ADDR)
    #启动服务器
    httpd.serve_forever()