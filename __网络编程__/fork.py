import os
from time import sleep
print('=====================')
pid = os.fork()
if pid < 0:
    priont('创建进程失败!!!!!')
elif pid == 0:
    sleep(1)
    print('新创建的进程')
else:
    sleep(3)
    print('原来的进程')
print('程序执行完毕')
