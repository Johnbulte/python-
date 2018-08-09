#coding=utf-8
from views import *

'''
功能 : 完成后端请求处理服务代码
说明 : 模拟Web框架的基本原理
'''
#设置静态网页文件夹
STATIC_DIR = './static'
#Python方法
METHOD_DIR = './wsgiPy'

#应用类
class Application(object):
    def  __init__(self,urls):
        self.urls = urls 
    
    def __call__(self,env):
        method = env.get('METHOD','GET')
        path = env.get('PATH_INFO','/')  #请求内容

        if path == '/' or path[-5:] == '.html':
            response = self.get_html(path)
        else:
            response = self.get_data(path)

        return response

    def get_html(self,path):
        if path == '/':
            get_file = STATIC_DIR + "/index.html"
        else:
            get_file = STATIC_DIR + path 

        try:
            fd = open(get_file)
        except IOError:
             #没有找到页面
            responseHeaders = "HTTP/1.1 404 not found\r\n"
            responseHeaders += "\r\n"
            responseBody = "===Sorry,the page not found==="
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n" 
            responseBody = fd.read()
        finally:
            response = responseHeaders + responseBody
            return response 

    def get_data(self,path):
        for url,handler in self.urls:
            if path == url:
                return handler()

        responseHeaders = "HTTP/1.1 404 not found\r\n"
        responseHeaders += "\r\n"
        responseBody = "===Sorry,the data not found==="
        return responseHeaders + responseBody

urls = [
    ('/time',show_time),
    ('/hello',say_hello),
    ('/bye',say_bye)
]

app = Application(urls)