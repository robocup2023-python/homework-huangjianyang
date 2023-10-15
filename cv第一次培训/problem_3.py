import cv2 as cv
import sys
import numpy as np
def judge(nums):
    if nums>=length:
        return nums-length
    return nums
if __name__=='__main__':
    #extension_len=int(input())
    extension_len=100
    img=cv.imread('test.png')
    length=len(img[0])
    length_new=extension_len*2+length
    img_new=np.zeros((length_new,length_new,3),dtype=np.uint8)
    for i in range(0,length):
        for j in range(0,length):
            img_new[i+extension_len][j+extension_len]=img[i][j]
    for i in range(0,extension_len):
        for j in range(extension_len,extension_len+length):
            img_new[i][j]=img_new[extension_len*2-i-1][j]
    for i in range(extension_len+length,extension_len*2+length):
        for j in range(extension_len,extension_len+length):
            img_new[i][j]=img_new[length*2+extension_len*2-i-1][j]
    for i in range(0,extension_len):
        for j in range(0,extension_len*2+length):
            img_new[j][i]=img_new[j][extension_len*2-i-1]
    for i in range(extension_len+length,extension_len*2+length):
        for j in range(0,extension_len*2+length):
            img_new[j][i]=img_new[j][length*2+extension_len*2-i-1]
    cv.imshow('test1',img_new)
    cv.waitKey(1000)
    length=len(img[0])
    length_new=extension_len*2+length
    img_new=np.zeros((length_new,length_new,3),dtype=np.uint8)
    for i in range(0,length_new):
        for j in range(0,length_new):
            img_new[i][j]=img[judge(i-extension_len)][judge(j-extension_len)]
    cv.imshow('test2',img_new)
    cv.waitKey(0)
    cv.destroyAllWindows()