__author__ = 'James'
import bluetooth
rumble_pack_address = None
server_socket = None
def setup():
    try:
        global rumble_pack_address
        rumble_pack_name = "HC-05"
        for retry in range(0,5):
            nearby_devices = bluetooth.discover_devices()
            for bdaddr in nearby_devices:
                if rumble_pack_name == bluetooth.lookup_name(bdaddr):
                    rumble_pack_address = bdaddr
                    print("found rumble_pack")
                    break
                
            
            if rumble_pack_address == None:
                print("rumble_pack not found, retrying...")
            else:
                break          

           
    except Exception as err:
         print(err)


def start():
    port = 1
    global server_socket
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.connect((rumble_pack_address,port))
    server_socket.send("1")

def stop():
    try:
	server_socket.close()
    except Exception:
	raise Exception("unable to stop")