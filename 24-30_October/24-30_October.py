# -*- coding: utf-8 -*-
"""
## 24-30_October
	Title: Basic image features and some techniques.
	Content: vector, indexing, noise, image of intensity, image features.
	Keywords: sum, .transpose, np.random.randint, .size, .dtype, .shape
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Some basic OpenCV functions.
path = r"C:\Users\umutf\Downloads\M5CS5K.jpg"#BE CAREFULL WITH PATH
img = cv2.imread(path)
cv2.imshow('image', img)
print(img.size) #image's size
print(img.dtype) #image's data type
print(img.shape) #image's height, width, and number of channels.
cv2.waitKey()
cv2.destroyAllWindows()

#Output:
# 44236800
# uint8
# (2880, 5120, 3)



# #Image of intesity: a matrix or image.
# row = 256
# col = 256
# img =np.zeros((row,col)) #an array consists of zero value.
# img[100:105, : ] = 0.5
# img[:, 100:105] = 1
# plt.figure(figsize=(10,4))
# plt.imshow(img)
# plt.show()

# #Noise: an image consisting of randomly placed black and white pixels.
# height = 512
# width = 512
# img = np.random.randint(255, size=(height, width, 1), dtype=np.uint8)
# cv2.imshow('image', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

#Indexing vectors
# v = [1,3,5,7,9]
# value = v[2] #5 is variable's value
# w = np.transpose(v)
# print(w)
# value = v[1:3] #getting values from different places.
# C = np.array([[1,1,2],[3,4,5],[9,8,7]])
# s = sum(C[:]) #same as sum(C). Both gets sum of selected indexes.
# print(s)
