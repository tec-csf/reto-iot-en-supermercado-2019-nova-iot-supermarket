from MagneticSensor import switch_puerta
from RFIDReader import RFID_Read
from TemperaturaDHT11 import temperatura
from Camara import camara
while(1):
    switch_puerta(3)
    RFID_Read()
    temperatura(2)

    if estado_puerta == True and RFID_Read == True:
        print("ALERTA")