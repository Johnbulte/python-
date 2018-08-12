#计算密集型
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1
#IO密集型
def write():
    f = open('text.txt','w')
    for x in range(1000000):
        f.write('hell world\n')
    f.close()
def read():
    f = open('text.txt')
    lines = f.readlines()
    f.close()