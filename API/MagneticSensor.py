import time
import RPi.GPIO as io

door_pin = 3

def switch_puerta(door_pin):
    io.setwarnings(False)
    io.setmode(io.BCM)
    estado_puerta = "CLOSE"
    io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)
    if io.input(door_pin):
        estado_puerta = "OPEN"
        print("PUERTA ABIERTA!")
    else:
        print ("PUERTA CERRADA!")

    return estado_puerta

if __name__ == "__main__":
    while True:
        time.sleep(1)
        estado_puerta = switch_puerta(door_pin)
        print(f"Estado Puerta: {estado_puerta}")