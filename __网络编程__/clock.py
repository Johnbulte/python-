from multiprocessing import Process
import time
class ClockProcess(Process):
	def __init__(self,value):
		#调用父类的__init__
		super(ClockProcess,self).__init__()
		self.value = value
	#重写run方法
	def run(self):
		for i in range(5):
			time.sleep(self.value)
			print('This time is {}'.\
				format(time.ctime()))
#用自己的类创建一个进程对象
p = ClockProcess(2)
#自动执行run
p.start()
p.join()