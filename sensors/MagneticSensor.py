import time
import RPi.GPIO as io

def switch_puerta(door_pin):

    estado_puerta = False
    io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
    if io.input(door_pin):
        estado_puerta = True
        print("PUERTA ABIERTA!")
        time.sleep(0.5)
    else:
        print ("PUERTA CERRADA!")
        time.sleep(0.5)
    return estado_puerta