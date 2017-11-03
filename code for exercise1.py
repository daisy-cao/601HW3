import cv2

img=cv2.imread('C:\Users\caoyu\Desktop\lenna.png')
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
