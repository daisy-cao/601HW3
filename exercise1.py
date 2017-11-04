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
h,s,v=cv2.split(img1)
cv2.imshow('h',h)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('s',s)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('v',v)
cv2.waitKey(0)
cv2.destroyAllWindows()
img2=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
y,cr,cb=cv2.split(img2)
cv2.imshow('y',y)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('cr',cr)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('cb',cb)
cv2.waitKey(0)
cv2.destroyAllWindows()

pi=img[20,25]
pi1=img1[20,25]
pi2=img2[20,25]
print(pi)
print(pi1)
print(pi2)
