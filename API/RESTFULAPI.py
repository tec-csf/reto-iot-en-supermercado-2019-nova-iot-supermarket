#!/usr/bin/python
import datetime
import _thread
import time
import jwt
import paho.mqtt.client as mqtt
import random
from Camara import camara
from TemperaturaDHT11 import temperatura
from MagneticSensor import switch_puerta
from RFIDReader import RFID_Read
from SensorMovimiento import mov

#--------------------------------Variables de sensores------------------------------------------------------------------------------
motion_sensor_pin = 26
motion_led_pin = 19


#--------------------------------Variables del Proyecto------------------------------------------------------------------------------
ssl_private_key_filepath = '/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/API/demo_private.pem'
ssl_algorithm = 'RS256'  # Either RS256 or ES256
root_cert_filepath = '/home/pi/iot_supermercado/reto-iot-en-supermercado-2019-nova-iot-supermarket/API/roots.pem'
project_id = 'nova-semana-i'
gcp_location = 'us-central1'
registry_id = 'semana-i'
device_id = 'rpi'
#------------------------------------------------------------------------------------------------------------------------------------
# Tiempo Actual
cur_time = datetime.datetime.utcnow()

# Crear JWT
def create_jwt():
    token = {
        'iat': cur_time,
        'exp': cur_time + datetime.timedelta(minutes=60),
        'aud': project_id
    }

    with open(ssl_private_key_filepath, 'r') as f:
        private_key = f.read()

    return jwt.encode(token, private_key, ssl_algorithm)


_CLIENT_ID = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(
    project_id, gcp_location, registry_id, device_id)
_MQTT_TOPIC = '/devices/{}/events'.format(device_id)

client = mqtt.Client(client_id=_CLIENT_ID)
# authorization is handled purely with JWT, no user/pass, so username can be whatever
client.username_pw_set(
    username='unused',
    password=create_jwt())

def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))

def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))

def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')


client.on_connect = on_connect
client.on_publish = on_publish

# Replace this with 3rd party cert if that was used when creating registry
client.tls_set(ca_certs=root_cert_filepath)
client.connect('mqtt.googleapis.com', 443)
client.loop_start()

# Could set this granularity to whatever we want based on device, monitoring needs, etc
#
#--------------------------------------------SENSORES---------------------------------------------------------------------------

#--------------------------------------------Callback-------------------------------------------------------
while (True):
    print ("Iniciar el while")
    temperature,humidity = temperatura(13)
    estado_puerta = switch_puerta(6)
    movimiento = mov(motion_sensor_pin, motion_led_pin)
    print(f"PUERTA: {estado_puerta} | MOVIMIENTO: {movimiento}")
    if (estado_puerta == 'OPEN' and movimiento):

        print("Proceso Camara")
        edad, genero = camara()
        #_thread.start_new_thread(check_product, ("Checking Product"))
        print("Checking")
        id_tag, des_tag = RFID_Read()
    #-------------------------------SEND PAYLOAD--------------------------------------------------
        payload = '{{ "ts": {}, "edad": {}, "genero": "{}", "temperature": {}, "humidity": {}, "estado_puerta": "{}","id_tag": {},"des_tag": "{}" }}'.format(
            int(time.time()), str(edad), str(genero),temperature,humidity,str(estado_puerta),id_tag, str(des_tag))
    # Uncomment following line when ready to publish
        client.publish(_MQTT_TOPIC, payload, qos=1)
        #-----------------------------------------------------------------------------------------------------------
        print("{}\n".format(payload))
        time.sleep(1)
        client.loop_stop()