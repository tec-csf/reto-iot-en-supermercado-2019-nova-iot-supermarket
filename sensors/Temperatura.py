import RPi.GPIO as GPIO
import time
import pyrebase
import subprocess
from datetime import datetime
from pprint import pprint
import sys
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
#humedad
pin = 2
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(chanel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(led_pin, GPIO.OUT)

def humCallback(pin):
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        print(humedad)
        print("\t")
        print(temperatura)
        if temperatura >21:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)

while True:
    humCallback(pin)
