v=input().split()
for i in range(len(v)):
    v[i]=int(v[i])
nums=int(input())
v.append(nums)
for i in range(len(v)-1,0,-1):
    if v[i]<v[i-1]:
        tmp=v[i]
        v[i]=v[i-1]
        v[i-1]=tmp
print(v)