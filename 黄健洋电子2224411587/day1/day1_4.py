for i in range(1,10):
    for j in range(1,i+1):
        if i==j:
            print(i,'*',j,'=',i*j,sep='',end='\n')
        else:
            print(i,'*',j,'=',i*j,sep='',end=' ')