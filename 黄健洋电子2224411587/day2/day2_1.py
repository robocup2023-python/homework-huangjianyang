s=input()
a=0
b=0
c=0
d=0
for i in s:
    if i.isalpha()==True:
        a+=1
    elif i.isdigit()==True:
        b+=1
    elif i==' ':
        c+=1
    else:
        d+=1
print('英文字符数：',a)
print('数字字符数：',b)
print('空格字符数：',c)
print('其他字符数：',d)