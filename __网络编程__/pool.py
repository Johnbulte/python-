#pool.py
from multiprocessing import Pool
from time import sleep,ctime
#事件函数
def worker(msg):
	sleep(2)
	print(msg)
	return msg + 'over'
#创建进程池
pool = Pool(processes = 4)
result = []
for i in range(10):
	msg = 'hello %d'%i
	#将事件放入进程池
	
	r = pool.apply_async(func = worker,args=(msg,))
	result.append(r)
#关闭进程池
pool.close()
#回收进程池
pool.join()
for i in result:
	print(i.get())