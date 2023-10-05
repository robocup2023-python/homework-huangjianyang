v=[]
v.extend([1,1])
for i in range(18):
    v.append(v[-1]+v[-2])
print(v)