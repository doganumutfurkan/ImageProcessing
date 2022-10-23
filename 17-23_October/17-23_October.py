"""
Date:
    17-23_October
Title: 
    Introduction to Python, NumPy and OpenCv
Content: 
    Fundamentals of Python, NumPy and OpenCv; such as loops, lists, array operations,
    defining a function, etc.
Keywords:
    cv2.imread, np.array, .dtype, ndim, .shape, .reshape, .random, randint,
    .copy, .arenge, np.zeros, np.eye, indexing, mean, around, for loop

"""

# #OPENCV TEST SCRIPT
# import cv2
# path = r"C:\Users\umutf\Downloads\M5CS5K.jpg"#BE CAREFULL WITH PATH
# img = cv2.imread(path)
# cv2.imshow('image', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

"""

###Numpy
import numpy as np
firstList = [23,10,22]
print(firstList)
numpyArray1 = np.array([1,2,3,4,5,6]) #it doesn't matter wheter using square bracket or not.
print(numpyArray1)
print(type(numpyArray1)) 
print(numpyArray1.dtype) #showing data type
#to casting the data type:
numpyArray2 = np.array([1,2,3], dtype = float)
print(numpyArray2.dtype)
twoDimentionArray = np.array([[1,2,3],[4,5,6]]) # two dimention list
print(twoDimentionArray.ndim) #dimention of list
threeDimentionArray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(threeDimentionArray.ndim)
print(twoDimentionArray, end = '\n\n')
print(threeDimentionArray)
print(twoDimentionArray.shape) #output is two lines and three columns
#we can change dimension of lists. Here is how:
numpyArray1 = numpyArray1.reshape(6,1)
#index quantity(eleman sayısı) of two arrays must be equal on both sides: 2x3=6 1x6=6
#when deifining (6,) it acts like (1,6). Don't know why.
print(numpyArray1)
#array oluşturmak:
newArray1 = np.arange(0,17,2)
#Start from zero, increase by 2 till 17 and don't include 17.
print(newArray1)
#To copy an array
newArray2 = newArray1.copy()
print(newArray2)
#Random arrays
newArray1 = np.random.random((3,3))
#two dimensional array which consists of random numbers between zero and one.
print(newArray1) 
#if you want to set boundaries:
newArray1 = np.random.randint(78, size = 9)
#values variying between zero to 77, index quantitiy is 9.
print(newArray1)
#getting specific lines and columns
firstLine = twoDimentionArray[0] #for second use 1
firstTwoLines = twoDimentionArray[0:2] 
print(firstLine)
print(firstTwoLines)
firstColumn = twoDimentionArray[:,0] #for second use 1
print(firstColumn)
myIndex = twoDimentionArray[1,2] #index of first line second column
print(myIndex)
#to getting reverse of an array:
twoDimentionArray = twoDimentionArray[ : : -1]
print(twoDimentionArray)
#array that consists of zeros
zeroArray = np.zeros((4,3)) #for 3 dimentions, write three numbers like (1,2,3)
print(zeroArray)
#to have cross line that consists of ones in zero array:
zeroArray = np.eye(4) #you have 4 ones in a croosing way
print(zeroArray)
# Source: 
# https://www.youtube.com/watch?v=63EHOcsYd5w&ab_channel=M%C3%BChendisinBlogu
# Continue from 15:00

"""

###Numpy Array Operations
from numpy.random import uniform
#random number array filled with pre-specified range
#works same way as np.arange
myArray = uniform(0,1,4)
print(myArray)
#for loop through array:
for number in myArray:
    print(number)

myArray = uniform(0,3,(3,3))
#between zero and 2, 3 by 3 array
print(myArray)
print(myArray[0][0])#same with [0,0]
#first columns:
for pair in myArray:
    print(pair[0])
#mean(ortalama) function
from numpy import mean
for numbers in myArray:
    print(mean(numbers))
#in this example it got mean of each line
#setting number of digits after comma
from numpy import around
for numbers in myArray:
    print(around(mean(numbers), 2))
#arounded to two digits
#Source:   
#https://www.youtube.com/watch?v=cNQ692g8NLw&ab_channel=GeroldBaier
   
