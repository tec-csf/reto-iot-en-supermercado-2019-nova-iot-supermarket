import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/sensors/MFRC522-python')
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
    text = input('Your Name:')
    print("Now place tag next to the scanner to write")
    id, text = reader.write(text)
    print("recorded")
    print(id)
    print(text)
finally:
    GPIO.cleanup()