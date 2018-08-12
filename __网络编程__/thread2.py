
# coding: utf-8

# In[4]:


from threading import Thread,currentThread
from time import sleep
#线程函数
def fun(sec):
    print('线程属性测试\n')
    sleep(sec)
    print('%s线程结束'%currentThread().getName())
thread = []
for i in range(3):
    t = Thread(target = fun,name = 'tedu%d'%i,              args = (3,))
    thread.append(t)
    t.start()
    print(t.is_alive())  #查看线程状态

#回收线程
for i in thread:
    i.join()

