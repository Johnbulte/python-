import time

def show_time():
    responseHeaders = "HTTP/1.1 200 OK\r\n"
    responseHeaders += "\r\n"
    responseBody = time.ctime()
    return responseHeaders + responseBody

def say_hello():
    responseHeaders = "HTTP/1.1 200 OK\r\n"
    responseHeaders += "\r\n"
    responseBody = "hello world"
    return responseHeaders + responseBody

def say_bye():
    responseHeaders = "HTTP/1.1 200 OK\r\n"
    responseHeaders += "\r\n"
    responseBody = "Good bye"
    return responseHeaders + responseBody
