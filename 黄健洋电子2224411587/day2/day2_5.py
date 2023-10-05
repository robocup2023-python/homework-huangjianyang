import math
for i in range(101,201):
    p=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            p=False
            break
    if p==True:
        print(i)