import cv2 as cv
img=cv.imread('test.png')
x=cv.Sobel(img,cv.CV_16S,1,0,3)
x=cv.convertScaleAbs(x)
y=cv.Sobel(img,cv.CV_16S,0,1,3)
y=cv.convertScaleAbs(y)
xy=x+y
cv.imshow('test',xy)
cv.waitKey(0)