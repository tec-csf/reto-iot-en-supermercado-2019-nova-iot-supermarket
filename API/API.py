import sys
import datetime
import time
import jwt
import paho.mqtt.client as mqtt
import random
import Adafruit_DHT
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from Magnetic Sensor import switch_puerta
from RFIDReader import RFID_Read

while(1):
    switch_puerta()
    RFID_Read()
    if estado_puerta == True and RFID_Read == True:
        print("ALERTA")
