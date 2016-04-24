'''launch sight code for raspberry pi'''
def main():
    import RPi.GPIO as gpio
    import bluetooth
    import time
    import PyGlow
    phone_name = "BenPhone"
    rumble_pack_name ="HC-05"
    controller_name = "MOCUTE-032_B50-0407"
    pyglow = PyGlow.PyGlow()

    phone_address = None
    rumble_pack_address = None
    controller_address = None

    nearby_devices = bluetooth.discover_devices()
    ##find device addresses
    for bdaddr in nearby_devices:
        if phone_name == bluetooth.lookup_name( bdaddr ):
            phone_address = bdaddr
            pyglow.color("Yellow:", 100)

        if rumble_pack_name == bluetooth.lookup_name( bdaddr ):
            rumble_pack_address = bdaddr
            pyglow.color("Orange:", 100)

        if controller_name == bluetooth.lookup_name( bdaddr ):
            controller_address = bdaddr
            pyglow.color("Green:", 100)
        
        if phone_address is not None and rumble_pack_address is not None and controller_address is not None:
            pyglow.color("Yellow:", 0)
            pyglow.color("Orange:", 0)
            time.sleep(3)
            pyglow.color("All:", 0) 


    #is the phone on and connected
    if phone_address != None:
    #start listening to the phone
        port = 3
        phone_s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        phone_s.connect((phone_address, port))

        while 1:
            text = raw_input()
            #some sort of exit code
            if text == "quit":
                s.send(text)
                break

        #Did the phone tell us to start?
            port2 = 1
            if text == "start":
            #send a message to the rumble pack
                rumble_s = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
                rumble_s.connect((rumble_pack_address, port2))
                time.sleep(50)
                rumble_s.send(1)

                #start the fan
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)

                #play the base wav file



#                #check if the phone told us to stop OR control stop
#                if :
#                #stop the fan
#                    #stop the base track

#                    #stop the rumble pack
#                    port = 1
#                    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#                    sock.connect((rumble_pack_address, port))
#                    sock.send(1)
#                    sock.close()



#else:
##Flash red or something
#None






if __name__ == '__main__':main()
