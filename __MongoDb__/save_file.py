from pymongo import MongoClient
import bson.binary
conn = MongoClient('localhost',27017)

db = conn.images
myset = db.jpg

#存储
f = open('file.jpg','rb')

#格式转换为mongodb能存储的格式

'''content = bson.binary.Binary(f.read())

myset.insert({'filename':'file.jpg','data':content})'''

#获取文件
data = myset.find_one({'filename':'file.jpg'})

with open(data['filename'],'wb') as f:
	f.write(data['data'])