from socket import *
import sys 
import time 

#功能封装为类
class TftpClient(object):
    def __init__(self,s):
        self.sockfd = s

    def do_list(self):
        self.sockfd.send(b"L")  #发送请求类型
        #等待服务器确认
        data = self.sockfd.recv(1024).decode()

        if data == 'OK':
            data = self.sockfd.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("%%%%%%文件展示完毕%%%%%%\n")
        else:
            #失败原因
            print(data)

    def do_get(self,filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)                
                if data == b"##":
                    break                   
                fd.write(data)
            fd.close()
            print("%s 下载完成\n"%filename)
        else:
            print(data)


    def do_put(self,filename):
        try:
            fd = open(filename,'rb')
        except:
            print("上传文件不存在")
            return

        self.sockfd.send(("P " + filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data == 'OK':
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            print("%s 文件上传完毕"%filename)
        else:
            print(data)


    def do_quit(self):
        self.sockfd.send(b'Q') 

#套接字连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket()
    s.connect(ADDR)
    tftp = TftpClient(s)

    while True:
        print("")
        print("========命令选项=======")
        print("******** list *******")
        print("****** get file *****")
        print("****** put file *****")
        print("******** quit *******")
        print("======================")

        cmd = input("请输入命令>>")

        if cmd.strip() == 'list':
            tftp.do_list()
        elif cmd[:3] == "get":
            filename = cmd.split(' ')[-1]
            tftp.do_get(filename)
        elif cmd[:3] == "put":
            filename = cmd.split(' ')[-1]
            tftp.do_put(filename) 
        elif cmd.strip() == "quit":
            tftp.do_quit()
            sys.exit("欢迎使用")
        else:
            print("请输入正确的命令！！！")
            continue

if __name__ == "__main__":
    main()
