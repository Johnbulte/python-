from pymongo import MongoClient
conn = MongoClient('localhost',27017)
db = conn.stu 
myset = db.class5

#创建索引
'''index = myset.ensure_index('name')  #返回索引名称'''

#创建复合索引

'''index = myset.ensure_index\
([('name',1),('King',-1)])'''

#创建其他类型索引
'''index = myset.ensure_index\
('name',unique = True,sparse = True)'''


#查看当前索引
'''for i in myset.list_indexes():
	print(i)'''

#删除索引
'''myset.drop_index('name_1')'''

#删除所有索引

'''myset.drop_indexes()'''

l = [{'$group':{'_id':'$King','num':{'$sum':1}}},
{'$match':{'num':{'$gt':1}}}
]
cursor = myset.aggregate(l)
for i in cursor:
	print(i)

conn.close()

