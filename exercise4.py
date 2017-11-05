
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('C:\Users\caoyu\Desktop\lenna.png',0)
plt.subplot(3,2,1),plt.imshow(img,'gray')
ret,thresh1 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
plt.subplot(3,2,2),plt.imshow(thresh1,'gray')
ret,thresh2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
plt.subplot(3,2,3),plt.imshow(thresh2,'gray')
ret,thresh3 = cv2.threshold(img,27,255,cv2.THRESH_BINARY)
ret,thresh4 = cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
plt.subplot(3,2,4),plt.imshow(thresh3+thresh4,'gray')
ret,thresh5 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

plt.subplot(3,2,5),plt.imshow(thresh5,'gray')
