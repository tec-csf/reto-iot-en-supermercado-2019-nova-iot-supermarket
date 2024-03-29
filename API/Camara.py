import RPi.GPIO as GPIO
import time
import pyrebase
import subprocess
from datetime import datetime
import requests
from pprint import pprint
import sys
import time

def camara():
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering

    subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/image.jpg', '-1'], shell=True)

    #Azure
    face_uri = "https://raspberrycp.cognitiveservices.azure.com/vision/v1.0/analyze?visualFeatures=Faces&language=en"
    pathToFileInDisk = r'/home/pi/Desktop/image.jpg'
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()

    headers = { "Content-Type": "application/octet-stream" ,'Ocp-Apim-Subscription-Key': '7e9cfbb244204fb994babd6111235269'}
    response = requests.post(face_uri, headers=headers, data=data)
    faces = response.json()
    pprint(faces)
    pprint(len(faces))
    faces_list = faces["faces"]
    for person in faces_list:
        edad = person["age"]
        genero = person["gender"]
        pprint(edad)
        pprint(genero)
    return (edad,genero)