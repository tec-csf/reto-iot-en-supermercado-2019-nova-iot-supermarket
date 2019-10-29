import cv2

while True:
    #Cambiar a funcion
    capture=cv2.VideoCapture(0)
    ret, frame= capture.read(0)
    cv2.imwrite('imagen.png', frame)
    cv2.imshow('video',frame)

    if cv2.waitkey(1)==27:
        break

capture.realease()
cv2.destroyAllWindows()
