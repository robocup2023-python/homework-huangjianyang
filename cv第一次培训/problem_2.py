import cv2 as cv
import numpy as np
import sys
if __name__=='__main__':
    size=int(input())
    if size%2==0:
        print('error')
        sys.exit(-1)
    sigma=float(input())
    G=cv.getGaussianKernel(size,sigma)
    kernal=G*G.T
    k=size//2
    img=cv.imread('test.png')
    length=len(img)
    img_new=np.zeros((length,length,3),dtype=np.uint8)
    for i in range(k,length-k):
        for j in range(k,length-k):
            for l in range(-k,k+1):
                for r in range(-k,k+1):
                    for p in range(3):
                        img_new[i][j][p]+=img[i+l][j+r][p]*kernal[l+k][r+k]
    cv.imshow('test',img_new)
    cv.waitKey(0)
    cv.destroyAllWindows()