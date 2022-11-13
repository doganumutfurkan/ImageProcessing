"""
## 07-13_November
	Title: Spatial Filtering
	Content: Smoothing spatial filters, Two smoothing
    averaging filter masks, Blur, Order-statistic (nonlienar) filters,
    Sharpening spatial filters, Laplace operator.
	Keywords: .filter2D, .blur, cv.boxFilter, .medianBlur, .concatenate, .Laplacian 
    Files: An image for observing results of functions, test.jpg
"""
import numpy as np
import cv2 as cv

img = cv.imread('test.jpg',0)

# #Two Smoothing Averaging Filter Masks
# kernel1 = np.ones((3, 3))
# img = cv.filter2D(src=img, ddepth=-1, kernel=kernel1)
# cv.imshow('Smoothing', img)

# #Blur an image with a 2D convolution matrix
# kernel1 = np.ones((5, 5), np.float32)/30
# result = cv.filter2D(src=img, ddepth=-1, kernel=kernel1)
# cv.imshow('Original', img)
# cv.imshow('Kernel Blur', result)

# Getting average of an image with cv.blur()
result = cv.blur(img,(3,3)) 

# Getting average of an image with cv.boxFilter()
result = cv.boxFilter(img, -1, (2,2),normalize = True)

#Order-statistic (Nonlinear) Filters
median = cv.medianBlur(img, 5)
compare = np.concatenate((img, median), axis =1)
laplacian = cv.Laplacian(img, -1)
    
cv.waitKey()
cv.destroyAllWindows()

