def judge(year):
    if year%400==0:
        return True
    elif year%100==0 and year%400!=0:
        return False
    elif year%4==0:
        return True
    return False
v=input().split()
year=int(v[0])
month=int(v[1])
day=int(v[2])
nums=[31,28,31,30,31,30,31,31,30,31,30,31]
if month==1:
    print(day)
if month==2:
    print(31+day)
day+=31+28
if judge(year):
    day+=1
for i in range(2,month-1):
    day+=nums[i]
print(day)
