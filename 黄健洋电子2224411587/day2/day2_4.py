for i in range(100,1000):
    nums=i
    count=0
    while nums>0:
        count+=(nums%10)**3
        nums//=10
    if count==i:
        print(i)
        