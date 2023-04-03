import cv2 as cv
import numpy as np
video=cv.VideoCapture("C:\Users\SIDDHARTHI\Downloads\Green screen cat.mp4")
image=cv.imread("C:\Users\SIDDHARTHI\Downloads\Fresh Cartoon Home Living Room Background Design.jpg")
# to keep both video and picture to same size
ret,frame=video.resize()
frame=cv.resize(frame,(640,480))
image=cv.resize(image,(640,480))
#To remove the upper green and lower green value from the range
u_green=np.array[140,153,70]
l_green=np.array[30,30,0]

# to create random matrix of 1b size
X=np.random.rand(1000000000)
import time #python library to use time
start =time.time()
mean=sum(X)/len(X)
print(time.time()-start)
#it'll give how much time it would take get the mean of 1b list
#To remove all green color
m =cv.inRange(frame,l_green,u_green)
#bitwise and to remove all except green
res =cv.bitwise_and(frame,frame,mask=m)#last to parameter are on whom op is applied
