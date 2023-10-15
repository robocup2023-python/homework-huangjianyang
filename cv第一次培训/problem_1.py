import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import sys
if __name__=='__main__':
    size=int(input())
    if size%2==0:
        print('error')
        sys.exit(-1)
    sigma=float(input())
    G=cv.getGaussianKernel(size,sigma)
    print('opencv标准高斯滤波核\n',G*G.T)
    x=np.array(([range(1,size+1)]))
    y=np.array(([range(1,size+1)])).T
    x_r, y_r=np.meshgrid(x,y)
    c=plt.pcolormesh(x_r,y_r,G*G.T,cmap='viridis_r')
    plt.show()
    v=np.zeros((size,size),dtype=np.float64)
    k=size//2
    for i in range(1,size+1):
        for j in range(1,size+1):
            v[i-1][j-1]=(0.5/np.pi/(sigma**2))*(np.e**(-((i-k-1)**2+(j-k-1)**2)/(2*(sigma**2))))
    print('人工高斯滤波核\n',v/np.sum(v))
    c=plt.pcolormesh(x_r,y_r,v/np.sum(v),cmap='viridis_r')
    plt.show()