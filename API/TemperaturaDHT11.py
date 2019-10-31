import Adafruit_DHT

def temperatura(pin_temp):
    sensor = Adafruit_DHT.DHT11
    temperature = 0
    if (temperature <=22):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin_temp)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}%  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
    return (temperature,humidity)