a=int(input())
ans=0
nums=a
for i in range(5):
    ans+=nums
    nums=nums*10+a
print(ans)