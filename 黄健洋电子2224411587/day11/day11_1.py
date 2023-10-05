import time
import threading
import os

for i in range(1,10):
    path=str(i)+'.txt'
    with open(path,'w') as f:
        f.write('1')
        f.close()

def rename(n: int) -> None:
    print(n)
    path=str(n)+'.txt'
    pathnew='python'+path
    os.rename(path,pathnew)
    time.sleep(2)

for i in range(1, 10):
    t = threading.Thread(target=rename, args=(i, ))
    t.start()
