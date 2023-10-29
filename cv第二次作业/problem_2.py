import cv2 as cv
import numpy as np
def NMS(magnitude, orientation):
    row, col = magnitude.shape
    out_edges = np.zeros_like(magnitude)
    for i in range(1, row - 1):
        for j in range(1, col - 1):
            angle = orientation[i, j]
            if angle < 0:
                angle += np.pi
            if (angle <= np.pi/8 or angle >= 7*np.pi/8):
                if magnitude[i, j] > magnitude[i, j - 1] and magnitude[i, j] > magnitude[i, j + 1]: 
                    out_edges[i, j] = magnitude[i, j]
            elif (angle > np.pi/8 and angle <= 3*np.pi/8) or (angle >= 5*np.pi/8 and angle < 7*np.pi/8): 
                if magnitude[i, j] > magnitude[i - 1, j - 1] and magnitude[i, j] > magnitude[i + 1, j + 1]:
                    out_edges[i, j] = magnitude[i, j]
            elif (angle > 3*np.pi/8 and angle < 5*np.pi/8): 
                if magnitude[i, j] > magnitude[i - 1, j] and magnitude[i, j] > magnitude[i + 1, j]: # 只检测上下两个像素点的数值
                    out_edges[i, j] = magnitude[i, j]
    return out_edges
sigma=float(input())
img=cv.imread('test.png',cv.IMREAD_GRAYSCALE)
img=cv.GaussianBlur(img,[3,3],sigma)
sobel_X=np.array([[-1,0,1],
                  [-2,0,2],
                  [-1,0,1]])
sobel_Y=np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]])
dx=cv.filter2D(img,cv.CV_64F,kernel=sobel_X)
dy=cv.filter2D(img,cv.CV_64F,kernel=sobel_Y)
arg=np.arctan2(dy,dx)
d=np.power(np.power(dx,2)+np.power(dy,2),1/2)
d_normal=cv.normalize(d,None,1,0,cv.NORM_INF)
cv.imshow('test',d_normal)
cv.waitKey(0)
img_nms=NMS(d_normal,arg)
cv.imshow('test',img_nms)
cv.waitKey(0)
img_new=cv.Canny(img,100,200,apertureSize=3)
cv.imshow('test',img_new)
cv.waitKey(0)