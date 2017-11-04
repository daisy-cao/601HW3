import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
img=cv2.imread('C:\Users\caoyu\Desktop\lenna.png',0)
a,b=img.shape
k=1
plt.figure(figsize=(10,10))
for mean in (0,5,10,20):
    for sigma in (0,20,50,100):
        temp=img
        gauss = np.random.normal(mean,sigma,img.shape)
        
        for i in range(a):
            for j in range(b):
                temp[i][j]+=gauss[i][j]
        plt.subplot(4,4,k),plt.imshow(img,'Greys_r')
        k+=1
temp=img
m=1
for pb in (0.01,0.03,0.05,0.4):
    for i in range(a):
        for j in range(b):
            rdn = random.random()
            if rdn < pb:
                temp[i][j] = 0
            elif rdn > (1-pb):
                temp[i][j] = 255
            else:
                temp[i][j] = img[i][j]
    plt.subplot(2,2,m),plt.imshow(temp,'Greys_r')
    m+=1
