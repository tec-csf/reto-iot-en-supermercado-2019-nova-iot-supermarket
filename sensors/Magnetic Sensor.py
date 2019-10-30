import time
import RPi.GPIO as io

def switch_puerta():
    io.setmode(io.BCM)

    door_pin = 4

    io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
    if io.input(door_pin):
        print("PUERTA ABIERTA!")
        time.sleep(0.5)
    else:
        print ("PUERTA CERRADA!")
        time.sleep(0.5)
