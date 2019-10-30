import cv2 as cv
import numpy as np

img = cv.imread('/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/opencvTests/images/download.jpeg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)

#print("Done")
while cv.waitKey(5) != 27:
    cv.imshow('asfsafda', edges)