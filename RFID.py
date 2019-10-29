import RPi.GPIO as GPIO
import time
import pyrebase
import subprocess
from datetime import datetime
from pprint import pprint
import sys
import time

card = '0019171125'
def main():
    while True:
        sys.stdin = open('/dev/tty0', 'r')
        RFID_input = input()
        if RFID_input == card:
            print "Access Granted"
            print "Read code from RFID reader:{0}".format(RFID_input)
        else:
            print "Access Denied"
            tty.close()
