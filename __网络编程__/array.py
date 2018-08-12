from multiprocessing import Process,Array
import time
#创建共享内存，存入列表
'''shm = Array('i',[1,2,3,4,5])'''
#表示开辟五个整形空间
shm = Array('i',5)
def fun():
	#shm是可迭代对象
	for i in shm:
		print(i)
		#修改共享内存
		shm[3] = 1000

p = Process(target= fun)
p.start()
p.join()
for i in shm:
	print(i)