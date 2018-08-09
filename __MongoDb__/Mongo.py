from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
#__getitem__    __setitem__
db = conn.stu 
'''db = conn['stu']'''

#创建集合对象
myset = db.class5
'''myset = db['class']'''

#操作数据库
#'''print(dir(myset))'''
#执行插入操作
'''myset.insert({'name':'张铁林','King':'乾隆'})'''
'''myset.insert([{'name':'张国立','King':'康熙'},\
	{'name':'陈道明','King':'康熙'}])'''

'''myset.insert_many([{'name':'唐国强','King':'雍正'},\
	{'name':'陈建斌','King':'雍正'}])'''
'''myset.insert_one({'name':'郑少秋','King':'乾隆'})'''
'''myset.save({'_id':1,'name':'吴奇隆','King':'四爷'})'''
#查找操作
cursor = myset.find({},{'_id':0})

'''for i in cursor:
	print(i['name'],'-----',i['King'])'''
#print(cursor.next())   #取下一个值
'''print(cursor.count())   #统计数量
print(cursor.limit(2))
print(cursor.skip(2))'''

#删除操作
'''myset.remove({'name':'冰冰'})

#只删除第一条符合条件的数据
myset.remove({'King':'乾隆'},multi = False)'''
print(myset.find_one_and_delete({'name':'吴奇隆'}))
#关闭数据库连接
conn.close()