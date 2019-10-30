import RPi.GPIO as GPIO
import sys
#sys.path.append('/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/sensors/MFRC522-python')
from mfrc522 import SimpleMFRC522

reader=SimpleMFRC522()
print("Hold a tag near the reader")
try:
    id,text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()