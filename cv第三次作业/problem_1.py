import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
def fft(img):
    img_height=img.shape[0]
    img_width=img.shape[1]
    height=cv.getOptimalDFTSize(img_height)
    width=cv.getOptimalDFTSize(img_width)
    top=int((height-img_height)/2)
    bottom=int(height-img_height-top)
    left=int((width-img_width)/2)
    right=int(width-img_width-left)
    appropriate=cv.copyMakeBorder(img,top=top,bottom=bottom,left=left,
                                  right=right,borderType=cv.BORDER_CONSTANT)
    flo=np.zeros(appropriate.shape,dtype='float32')
    com=np.dstack([appropriate.astype('float32'),flo])
    result=cv.dft(com,cv.DFT_COMPLEX_OUTPUT)
    magnitude_res=cv.magnitude(result[:,:,0],result[:,:,1])
    magnitude_log=np.log(magnitude_res)
    magnitude_res=magnitude_log[top:img_height,left:img_width]
    magnitude_norm=cv.normalize(magnitude_res,None,alpha=0,beta=1,norm_type=cv.NORM_MINMAX)
    magnitude_center=np.fft.fftshift(magnitude_norm)
    return magnitude_center
if __name__=='__main__':
    img=cv.imread('test.png')
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    f=np.fft.fft2(gray)
    fangle=np.angle(f)
    f=np.fft.fftshift(f)
    fmagnitude=np.log(np.abs(f))
    plt.figure(1)
    plt.imshow(fmagnitude,'gray')
    plt.title('magnitude')
    plt.figure(2)
    plt.imshow(fangle,'gray')
    plt.title('angle')
    plt.show()
    