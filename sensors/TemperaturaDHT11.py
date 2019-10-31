import Adafruit_DHT
sensor = Adafruit_DHT.DHT11

def temperatura(pin_temp):
    temperature = 0
    if (temperature <=22):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_temp)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
