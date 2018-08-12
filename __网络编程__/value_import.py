from multiprocessing import Process,Value
import time
import random
#创建共享内存对象
#初始值为2000
money = Value('i',2000)

#存钱
def deposite():
	for i in range(100):
		time.sleep(0.05)
		#对money value属性进行操作
		money.value += random.randint(1,200)

#取钱
def withdraw():
	for i in range(100):
		time.sleep(0.04)
		money.value -= random.randint(1,200)

d = Process(target = deposite)
w = Process(target = withdraw)

d.start()
w.start()

d.join()
w.join()

#查看共享内存数据
print(money.value)

