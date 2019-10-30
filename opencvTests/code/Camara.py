import cv2
while (cv2.waitKey(5) != 27):
    capture = cv2.VideoCapture(0)
    ret,frame = capture.read(0)
    cv2.imshow("Age Gender Demo", frame)
