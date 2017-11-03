import cv2

img=cv2.imread('C:\Users\caoyu\Desktop\lenna.png')
b,g,r=cv2.split(img)
cv2.imshow('b',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('g',g)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('r',r)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
#cv2.imshow('img1',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
pi=img[20,25]
pi1=img1[20,25]
pi2=img2[20,25]
print(pi)
print(pi1)
print(pi2)
