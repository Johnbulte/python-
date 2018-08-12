from time import sleep
import os
from multiprocessing import Semaphore,Process
#创建信号量对象
sem = Semaphore(3)
def fun():
    print('进程%d等待信号量'%os.getpid())
    sem.acquire()
    print('进程%d等待信号量'%os.getpid())
    sleep(3)
    print('进程%d等待信号量'%os.getpid())
    sem.release()
jobs= []
for i in range(4):
    p = Process(target =fun )
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()