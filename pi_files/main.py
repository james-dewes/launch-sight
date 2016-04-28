'''launch sight code for raspberry pi'''
def main():
    import time
    import wind
    import vibration
    
    phone_name = "BenPhone"
    controller_name = "MOCUTE-032_B50-0407"
    #set up the pyhsical effects
	wind.setup()
	vibration.setup()
	shake.setup()
	
	#set up the controllers
	phone.connect()
	contoller.connect()

    phone_address = None
    e
    controller_address = None

    nearby_devices = bluetooth.discover_devices()
    ##find device addresses
    for bdaddr in nearby_devices:
        if phone_name == bluetooth.lookup_name( bdaddr ):
            phone_address = bdaddr
            print("Phone found...")

        if rumble_pack_name == bluetooth.lookup_name( bdaddr ):
            rumble_pack_address = bdaddr
            print("Rumble pack found...")

        if controller_name == bluetooth.lookup_name( bdaddr ):
            controller_address = bdaddr
            print("Controller found")
        

    while 1:
        text = input("Enter start to continue, or quit to finish...")
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
            print("Waiting for 20")
            time.sleep(20)
            rumble_s.send('1')
            wind.start()
            vibration.start()

            
            print("Stopping!")
            rumble_s.send('0')
            break

                



    else:
        print("Phone not found...")
##Flash red or something
#None






if __name__ == '__main__':main()
