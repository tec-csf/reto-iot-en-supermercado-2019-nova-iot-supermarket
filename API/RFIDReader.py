import RPi.GPIO as GPIO
import sys
import time
sys.path.append('/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/API/MFRC522-python')
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)

def RFID_Read():
    reader=SimpleMFRC522()
    buzzer=5
    GPIO.setup(buzzer,GPIO.OUT)
    print("Hold a tag near the reader")
    id_tag,des_tag = reader.read()
    print(id_tag)
    print(des_tag)
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer,GPIO.LOW)
    return (id_tag,des_tag)
    #return (True)
    GPIO.cleanup()