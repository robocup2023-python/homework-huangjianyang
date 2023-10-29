import cv2 as cv
import numpy as np
def count(gray,Ix2,Iy2,Ixy):
    row, col = gray.shape
    R_mat=np.zeros((row,col),dtype='float64')
    for i in range(row):
        for j in range(col):
            M=gray[i][j]*np.mat([[Ix2[i][j],Ixy[i][j]],[Ixy[i][j],Iy2[i][j]]])
            R=np.linalg.det(M)-0.04*(np.trace(M)**2)
            R_mat[i][j]=R
    return R_mat
img=cv.imread('test.png')
gray=cv.imread('test.png',cv.IMREAD_GRAYSCALE)
gray=cv.GaussianBlur(gray,[3,3],1)
sobel_X=np.array([[-1,0,1],
                  [-2,0,2],
                  [-1,0,1]])
sobel_Y=np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]])
Ix=cv.filter2D(gray,cv.CV_64F,kernel=sobel_X)
Iy=cv.filter2D(gray,cv.CV_64F,kernel=sobel_Y)
Ix2=Ix*Ix
Iy2=Iy*Iy
Ixy=Ix*Iy
Ix2=cv.GaussianBlur(Ix2,[3,3],3)
Iy2=cv.GaussianBlur(Iy2,[3,3],3)
Ixy=cv.GaussianBlur(Ixy,[3,3],3)
R=count(gray,Ix2,Iy2,Ixy)
dst = cv.dilate(R,None)
img[dst>0.1*dst.max()]=[0,0,255]
cv.imshow('test',img)
cv.waitKey(0)