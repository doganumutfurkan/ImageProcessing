"""
## 31-06_November
	Title: Histogram and some basic basic conversion functions
	Content: Checking image's contrast and equalizing it.
	Keywords: .equalizeHist, .hstack, .flatten, .max
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('histogram.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

img = cv.imread('histogram.jpg',0)
equ = cv.equalizeHist(img) #equalize histogram function
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('res.png',res)