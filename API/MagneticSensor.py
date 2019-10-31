import time
import RPi.GPIO as io
def switch_puerta(door_pin):
    estado_puerta = "CLOSE"
    io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
    if io.input(door_pin):
        estado_puerta = "OPEN"
        print("PUERTA ABIERTA!")
        time.sleep(0.5)
    else:
        print ("PUERTA CERRADA!")
        time.sleep(0.5)
    return estado_puerta