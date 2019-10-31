import RPi.GPIO as GPIO
import sys
sys.path.append('/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/API/MFRC522-python')
from mfrc522 import SimpleMFRC522

def RFID_Read():
    reader=SimpleMFRC522()
    print("Hold a tag near the reader")
    try:
        id_tag,des_tag = reader.read()
        print(id_tag)
        print(des_tag)
    finally:
        return (id_tag,des_tag)
            #return (True)
        GPIO.cleanup()