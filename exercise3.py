import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
img=cv2.imread('C:\Users\caoyu\Desktop\lenna.png',0)
a,b=img.shape
plt.figure(figsize=(5,20))
##add gaussian noise to img
m=1
for mean in (0,5,10,20):
    for sigma in (0,20,50,100):
        temp=img
        gauss = np.random.normal(mean,sigma,img.shape)
        
        for i in range(a):
            for j in range(b):
                temp[i][j]+=gauss[i][j]
        plt.subplot(4,4,m),plt.imshow(img,'Greys_r')
        m+=1
#add salt&pepper noise to filter
temp=img
m=1
for pa in (0.01,0.03,0.05,0.4):
    for i in range(a):
        for j in range(b):
            rdn = random.random()
            if rdn < pa:
                temp[i][j] = 0
            else:
                temp[i][j] = img[i][j]
    for pb in (0.01,0.03,0.05,0.4):
        for i in range(a):
            for j in range(b):
                rdn = random.random()
                if rdn < pb:
                    temp[i][j] = 255
                else:
                    temp[i][j] = img[i][j]
        plt.subplot(4,4,m),plt.imshow(temp,'Greys_r')
        m+=1
temp=img
gauss = np.random.normal(0,50,img.shape)  
for i in range(a):
    for j in range(b):
        temp[i][j]+=gauss[i][j]
#box filter
#for Guassian noise box filter has better results
blur=cv2.blur(temp,(3,3))
plt.subplot(5,2,1),plt.imshow(img,'Greys_r')
plt.subplot(5,2,2),plt.imshow(blur,'Greys_r')
blur=cv2.blur(temp,(5,5))
plt.subplot(5,2,3),plt.imshow(blur,'Greys_r')
blur=cv2.blur(temp,(7,7))
plt.subplot(5,2,4),plt.imshow(blur,'Greys_r')
#gaussian filter
blur=cv2.GaussianBlur(temp,(3,3),0)
plt.subplot(5,2,5),plt.imshow(blur,'Greys_r')
blur=cv2.GaussianBlur(temp,(5,5),0)
plt.subplot(5,2,6),plt.imshow(blur,'Greys_r')
blur=cv2.GaussianBlur(temp,(7,7),0)
plt.subplot(5,2,7),plt.imshow(blur,'Greys_r')
#median filter    
blur=cv2.medianBlur(temp,3)

plt.subplot(5,2,8),plt.imshow(blur,'Greys_r')
blur=cv2.medianBlur(temp,5)
plt.subplot(5,2,9),plt.imshow(blur,'Greys_r')
blur=cv2.medianBlur(temp,7)
plt.subplot(5,2,10),plt.imshow(blur,'Greys_r')
pa=pb=0.01
temp=img
for i in range(a):
    for j in range(b):
        rdn = random.random()
        if rdn < pa:
            temp[i][j] = 0
        else:
            temp[i][j] = img[i][j]
for i in range(a):
    for j in range(b):
        rdn = random.random()
        if rdn < pb:
            temp[i][j] = 255
        else:
            temp[i][j] = img[i][j]
#box filter
blur=cv2.blur(temp,(3,3))
plt.subplot(2,2,1),plt.imshow(img,'Greys_r')
plt.subplot(2,2,2),plt.imshow(blur,'Greys_r')
blur=cv2.blur(temp,(5,5))
plt.subplot(2,2,3),plt.imshow(blur,'Greys_r')
blur=cv2.blur(temp,(7,7))
plt.subplot(2,2,4),plt.imshow(blur,'Greys_r')
#Gaussian filter
blur=cv2.GaussianBlur(temp,(3,3),0)
plt.subplot(2,2,1),plt.imshow(img,'Greys_r')
plt.subplot(2,2,2),plt.imshow(blur,'Greys_r')
blur=cv2.GaussianBlur(temp,(5,5),0)
plt.subplot(2,2,3),plt.imshow(blur,'Greys_r')
blur=cv2.GaussianBlur(temp,(7,7),0)
plt.subplot(2,2,4),plt.imshow(blur,'Greys_r')
#median filter  
#for salt&pepper noise median filter has the best result
blur=cv2.medianBlur(temp,3)
plt.subplot(2,2,1),plt.imshow(img,'Greys_r')
plt.subplot(2,2,2),plt.imshow(blur,'Greys_r')
blur=cv2.medianBlur(temp,5)
plt.subplot(2,2,3),plt.imshow(blur,'Greys_r')
blur=cv2.medianBlur(temp,7)
plt.subplot(2,2,4),plt.imshow(blur,'Greys_r')
