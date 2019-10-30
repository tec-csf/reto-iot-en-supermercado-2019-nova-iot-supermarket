import RPi.GPIO as GPIO
import time
import subprocess
from datetime import datetime
from pprint import pprint
import sys
import time

card = ''
counter = 1
while True:
    rfid = open('/dev/bus/usb/001/021', 'rb')
    RFID_input = rfid.read()
    #RFID_output = rfid.write(card)
    print(f"read {counter}: ", RFID_input)
    counter += 1
    time.sleep(2)
    if RFID_input == card:
        print ("Access Granted")
        print ("Read code from RFID reader:{0}".format(RFID_input))
        break
    else:
        print ("Access Denied")
rfid.close()
