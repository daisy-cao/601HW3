# 601HW3
## Exercise1
## How does a program read the cvMat object, in particular, what is the order of the pixel structure?

Mat has two data parts: the matrix header (containing information such as the size of the matrix, the method used for storing, at which address is the matrix stored, and so on) and a pointer to the matrix containing the pixel values (taking any dimensionality depending on the method chosen for storing) 

## Exercise2
![Alt text](https://user-images.githubusercontent.com/31779733/32462180-7dea8492-c306-11e7-89dc-607fcd2e3c7d.png)


[106 122 225]


[  4 135 225]


[151 181 103]

## Exercise 3
Gaussian Noise filter for mean={0,5,10,20},sigma={0,20,50,100}


![Alt text](https://user-images.githubusercontent.com/31779733/32462936-352f7fc0-c309-11e7-9634-7e63a144bc02.png
)

Salt&Pepper Noise
![Alt text](https://user-images.githubusercontent.com/31779733/32463003-72724c46-c309-11e7-9ce4-f035871c6870.png
)

Add different filter to Gaussian noise, and seems for Guassian noise, box filter has better results


![Alt text](https://user-images.githubusercontent.com/31779733/32463069-aaa1706a-c309-11e7-8d2a-1385e5443d46.png
)

Add different filter to Salt&Pepper Noise, and seems median filter has better results
![Alt text](https://user-images.githubusercontent.com/31779733/32463246-39ec2c10-c30a-11e7-878a-2beb417f52b4.png)

## Exercise 4
