# 601HW3
## Exercise1 How does a program read the cvMat object, in particular, what is the
## order of the pixel structure?

Mat has two data parts: the matrix header (containing information such as the size of the matrix, the method used for storing, at which address is the matrix stored, and so on) and a pointer to the matrix containing the pixel values (taking any dimensionality depending on the method chosen for storing) 

