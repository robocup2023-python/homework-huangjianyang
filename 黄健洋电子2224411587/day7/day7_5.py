import os
import random
i=int(input())
j=int(input())
for x in range(i):
    path='test'+str(x)+'.txt'
    with open(path,'w') as f:
        for y in range(j):
            nums=random.randint(1,126)
            while nums<33:
                nums=random.randint(1,126)
            f.write(chr(nums)+'\n')
        f.close()
    
for x in range(i):
    path='test'+str(x)+'.txt'
    pathnew='test'+str(x)+'python.txt'
    os.rename(path,pathnew)
    with open(pathnew,'a+') as f:
        f.write('python')
        f.close()
