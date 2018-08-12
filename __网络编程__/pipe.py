from multiprocessing import Process,Pipe
import os,time
#创建管道
fd1,fd2 = Pipe()#默认为双向管道
def fun(name):
	time.sleep(3)
	#向管道写入内容
	fd1.send('hello'+str(name))
jobs = []
for i in range(5):
	p = Process(target = fun,args=(i,))
	jobs.append(p)
	p.start()
for i in range(5):
	data = fd2.recv()
	print(data)

for i in jobs:
	i.join()
