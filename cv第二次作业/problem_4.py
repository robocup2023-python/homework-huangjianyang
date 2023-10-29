import cv2 as cv
from matplotlib import pyplot as plt
def count(v):
    n=len(img)
    m=len(img[0])
    v=[0 for _ in range(256)]
    for i in range(n):
        for j in range(m):
            v[img[i][j]]+=1
    change=[0 for _ in range(len(v))]
    all=n*m
    for i in range(len(v)):
        v[i]/=all
    for i in range(1,len(v)):
        v[i]+=v[i-1]
    for i in range(len(v)):
        v[i]*=len(v)-1
        change[i]=int(v[i])
    return change
img=cv.imread('test.png')
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.hist(img.ravel(),256,[0,256])
plt.title('origin img')
plt.show()
change=count(img)
img_result=cv.equalizeHist(img)
for i in range(len(img)):
    for j in range(len(img[0])):
        img_result[i][j]=change[int(img[i][j])]
plt.hist(img_result.ravel(),256,[0,256])
plt.title('equalized img')
plt.show()
plt.imshow(img_result,cmap='gray')
plt.show()