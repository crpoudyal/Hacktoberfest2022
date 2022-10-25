###Importing the OpenCV library
##import cv2
##from matplotlib import pyplot as plt
##
###Reading the image using imread() function
##image = cv2.imread('image.png')
##cv2.imshow("Amna",image)
### Extracting the height and width of an image
##h, w= image.shape[:2]
### Displaying the height and width
##print("Height = {}, Width = {}".format(h, w))

#######################################################
#######################################################

#####Importing the OpenCV library
##import cv2
####
#####Reading the image using imread() function
##image = cv2.imread('image.png')
##### Extracting RGB values. Here we have randomly chosen a pixel by passing in 100, 100 for height and width.
##(B, G, R) = image[100, 100]
####
##### Displaying the pixel values
##print("R = {}, G = {}, B = {}".format(R, G, B))

#######################################################
#######################################################

###Importing the OpenCV library
##import cv2
#####Reading the image using imread() function
##image = cv2.imread('image.png')
### We will calculate the region of interest by slicing the pixels of the image
##roi = image[100 : 500, 200 : 700]
##cv2.imshow("roi",roi)

#######################################################
#######################################################
##
###Importing the OpenCV library
##import cv2
#######Reading the image using imread() function
##readimg = cv2.imread('image.png')
### resize() function takes 2 parameters, the image and the dimensions
##resize_IMG = cv2.resize(readimg, (800, 800))
##cv2.imshow("RESIZE",resize_IMG)

#######################################################
#######################################################
###Importing the OpenCV library
##import cv2
###Reading the image using imread() function
##reading = cv2.imread('image.png')
### Using the rectangle() function to create a rectangle.
##rectangle = cv2.rectangle(reading, (1500, 900), (600, 400), (70, 56, 0), 4)
##
##cv2.imshow("Frame",rectangle)

#######################################################
#######################################################

##Importing the OpenCV library
##import cv2
## path to input images are specified and images are loaded with imread command
##image1 = cv2.imread('image1.png')
##image2 = cv2.imread('image2.png')
##
## cv2.addWeighted is applied over the
## image inputs with applied parameters
##weightedSum = cv2.addWeighted(image1, 1, image2, 1, 0)
##
## the window showing output image
## with the weighted sum
##cv2.imshow('Weighted Image', weightedSum)


#######################################################
#######################################################
##
### organizing imports
##import cv2
##import numpy as np
##
### path to input images are specified and
### images are loaded with imread command
##sub2 = cv2.imread('sub2.png')
##sub1 = cv2.imread('sub1.png')
##
### cv2.subtract is applied over the
### image inputs with applied parameters
##sub = cv2.subtract(sub1,sub2)
##
### the window showing output image
### with the subtracted image
##cv2.imshow('Subtracted Image', sub)

#######################################################
#######################################################
##
### organizing imports
import cv2
# Copying the original image
image2 = cv2.imread('image2.png')
cv2.imshow("Original",image2)

# Adding the text using putText() function
abc = cv2.putText(image2, 'Learning Python', (20,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

cv2.imshow("Text",abc)



















