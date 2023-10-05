def cacluate(*arg):
    count=0
    for i in arg:
        count+=i
    count/=len(arg)
    v=[]
    for i in range(len(arg)):
        if arg[i]>count:
            v.append(i)
    return (count,tuple(v))
print(cacluate(1,2,3,4))