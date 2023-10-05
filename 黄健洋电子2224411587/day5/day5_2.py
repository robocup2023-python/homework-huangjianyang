def get(v):
    i=1
    r=[]
    while i<len(v):
        r.append(v[i])
        i+=2
    return r
v=input().split()
for i in range(len(v)):
    v[i]=int(v[i])
print(get(v))