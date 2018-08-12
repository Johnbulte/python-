
# coding: utf-8

# In[5]:


#exit


# In[5]:


#dir(threading)


# In[9]:


import threading
from time import sleep
import os
a = 1
#线程函数
def music():
    global a
    a = 10000
    for i in range(5):
        sleep(2)
        print('播放葫芦娃',os.getpid())
#创建线程对象
t = threading.Thread(target = music)
t.start()
for i in range(5):
    sleep(1.5)
    print('想听扶摇',os.getpid())
t.join()
print('a=',a)

