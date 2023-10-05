import random
import shutil
with open('test.txt','w') as f:
    i=random.randint(1,100)
    for j in range(i):
        nums=random.randint(1,126)
        while nums<33:
            nums=random.randint(1,126)
        f.write(chr(nums)+'\n')
    f.close()

path='test.txt'
pathnew='copy_test.txt'
shutil.copy(path,pathnew)