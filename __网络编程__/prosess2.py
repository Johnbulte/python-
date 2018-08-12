from multiprocessing import Process
from time import sleep
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("T'm working......")
#通过args给函数传参
#通过kwargs给函数传参
p = Process(target = worker,args=(2,'levi'))
p.start()
#判断进程状态
print('is alive',p.is_alive())
#进程名
print('进程名是:',p.name)
#子进程PID
print('进程PID是:',p.pid)
p.join()
