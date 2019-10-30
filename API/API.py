from MagneticSensor import switch_puerta
from RFIDReader import RFID_Read

while(1):
    switch_puerta(3)
    RFID_Read()
    if estado_puerta == True and RFID_Read == True:
        print("ALERTA")