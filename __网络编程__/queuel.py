from multiprocessing import Queue
from time import sleep
#创建消息队列
q = Queue(3)
q.put(1)
sleep(0.1)
print(q.empty())
print(q.full())
q.put(2)
q.put(3)
print(q.qsize())
print(q.full())
print(q.get())
print(q.qsize())
q.close()