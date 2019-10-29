import RPi.GPIO as GPIO
import time
import pyrebase
import subprocess
from datetime import datetime
from pprint import pprint
import sys
import time
import Adafruit_DHT
#OpenCV for webcam
import cv2

# Configuracion del tipo de sensor DHT
sensor = Adafruit_DHT.DHT11
#humedad
pin = 2
#button camera
chanel = 3
#led_pin
led_pin=12
#button presencia alimento
chanelFood = 8




flagFood = False

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(chanel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(led_pin, GPIO.OUT)

# def callbackCamera(chanel):

#         if GPIO.input(chanel) == GPIO.HIGH:
#                 subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/image.jpg', '-1'], shell=True)
#                 #delete photo.
#                 #subprocess.call(['rm /home/pi/Desktop/image.jpg', '-1'], shell=True)

def humCallback(pin):
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        if temperatura >21:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

# def button_callback():
#         print(flagFood)
#         if GPIO.input(8) == 0 and flagFood == False:
#             print("Slot 1: Vacio")
#             self.flagFood = True
#             time.sleep(1)
#         if GPIO.input(8) == 1 and flagFood == False:
#             flagFood = True
#             print("Slot 1: Coca-Cola")
#             time.sleep(1)

#https://www.learnopencv.com/age-gender-classification-using-opencv-deep-learning-c-python/
while True:
    humCallback(pin)
    #Cambiar a funcion
    capture=cv2.VideoCapture(0)
    ret, frame= capture.read(0)
    cv2.imwrite('imagen.png', frame)
    cv2.imshow('video',frame)

    if cv2.waitkey(1)==27:
        break

capture.realease()
cv2.destroyAllWindows()
#     button_callback()
