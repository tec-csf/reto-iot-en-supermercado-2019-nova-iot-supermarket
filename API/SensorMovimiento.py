# Basic testing on presence sensor
#
# Author : Jorge Lopez
# Date   : 12/05/2019

# Import required Python libraries
import time
import RPi.GPIO as GPIO

motion_sensor_pin = 26
motion_led_pin = 5

def mov(GPIO_PIR, led_pin):
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set pin as input
    GPIO.setup(GPIO_PIR, GPIO.IN)
    GPIO.setup(led_pin, GPIO.OUT)
    try:
        movimiento = GPIO.input(GPIO_PIR)
        if movimiento == True:
            GPIO.output(led_pin, GPIO.HIGH)
            print("Se detecta  presencia")
            time.sleep(0.5)
        else :
            GPIO.output(led_pin, GPIO.LOW)
            print("No hay presencia")
            time.sleep(0.5)
    except:
        print("Movimiento: Failed to do GPIO.input")
    # Reset GPIO settings
    GPIO.cleanup()
    return (movimiento)

if __name__ == "__main__":
    while True:
        movimiento = mov(motion_sensor_pin, motion_led_pin)
        print(f"Movimiento: {movimiento}")