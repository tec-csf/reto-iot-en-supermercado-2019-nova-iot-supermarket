import time

def main():
    counter = 0
    card = ''
    with open('/dev/bus/usb/001/021', 'rb') as tty:
        while True:
            RFID_input = tty.readline()
            print(f"read {counter}: ", RFID_input)
            counter += 1
            time.sleep(2)
            if RFID_input == card:
                print("Access Granted")
                print("Read code from RFID reader:{0}".format(RFID_input))
            else:
                print("Access Denied")
                
main()