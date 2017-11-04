import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('C:\Users\caoyu\Desktop\lenna.png',0)
a,b=img.shape
m=1
plt.figure(figsize=(10,10))
for mean in (0,5,10,20):
    for sigma in (0,20,50,100):
        temp=img
        gauss = np.random.normal(mean,sigma,img.shape)
        
        for i in range(a):
            for j in range(b):
                temp[i][j]+=gauss[i][j]
        plt.subplot(4,4,m),plt.imshow(img,'Greys')
        m+=1
