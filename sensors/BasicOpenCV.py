import cv2# import opencv library
#reading the image
img=cv2.imread('messi.jpg',0)#read the image as grayscale image
#display in screen
cv2.imshow('messi',img)
k=cv2.waitKey(0) & 0xFF
if k==27:
cv2.destroyAllWindows()#close all display windows
elif k==ord('s'): #wait for 's' to be pressed
#save the image into new file
cv2.imwrite('messigray.png',img)
cv2.destroyAllWindows()