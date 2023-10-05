import csv
import random
with open('example.csv','w') as f:
    file=csv.writer(f)
    for i in range(10):
        v=[]
        for j in range(3):
            v.append(random.randint(1,100))
        file.writerow(v)
    f.close()
with open('example.csv','r') as f:
    file=csv.reader(f)
    v=[]
    sum=0
    for i in file:
        v.append(int(i[1]))
        sum+=v[-1]
    v.sort()
    print(max(v),min(v),sum/len(v),(v[4]+v[5])/2)