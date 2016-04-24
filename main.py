'''launch sight code for raspberry pi'''
def main():
    import bluetooth
    import time
    import winsound
    phone_name = "BenPhone"
    rumble_pack_name ="HC-05"
    controller_name = "MOCUTE-032_B50-0407"


    phone_address = None
    rumble_pack_address = None
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
            print("Playing wav!")

            #play the base wav file
            winsound.PlaySound("launch bass boost long.wav", winsound.SND_FILENAME)
            print("Stopping!")
            rumble_s.send('0')
            break

                



    else:
        print("Phone not found...")
##Flash red or something
#None






if __name__ == '__main__':main()
