#文件分开复制，只复制文件的一半
import os
from multiprocessing import Process
size = os.path.getsize('./img.jpg')
def copy1(filename):
	fr = open(filename,'rb')
	n = size // 2
	fw = open('copy1.jpg','wb')
	while True:
		if n < 1024:
			data = f.read(n)
			fw.write(data)
			break
		data f.read(1024)
		fw.write(data)
		n -= 1024
		fr.close()
		fw.close()
def copy2(filename):
	fr = open(filename,'rb')
	fw = open('copy2.jpg','wb')
	fr.seek(size // 2,0)#文件偏移位置到中间
	while True:
		data = fr.read(1024)
		if not data:
			break
		fw.write(data)
	fw.close()
	fr.close()
p1 = Process(target = copy1,args = ('img.jpg',))
p2 = Process(target = copy2,args = ('img.jpg',))
p1.start()
p2.start()

p1.join()
p2.join()