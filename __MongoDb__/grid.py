from pymongo import MongoClient
import gridfs

conn = MongoClient('localhost',27017)

db = conn.movie  #库名 

#通过GridFS获取集合对象
#fs 即为存储大文件对象
fs = gridfs.GridFS(db)

#通过查找获取游标

cursor = fs.find()

for file in cursor:
	if file.filename =='001、AI时代首选Python.ev4':
		with open(file.filename,'wb') s f:
			while True:
				data = file.read(4096)
				if not data:
					break
				f.write(data)
conn.close()