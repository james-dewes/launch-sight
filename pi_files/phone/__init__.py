__author__ = 'James'
import bluetooth
phone_address = None
def setup():
    try:
        global phone_address
        phone_name = "Nexus 5"
        for retry in range(0,5):
            nearby_devices = bluetooth.discover_devices()
            for bdaddr in nearby_devices:
                if phone_name == bluetooth.lookup_name(bdaddr):
                    phone_address = bdaddr
                    print("found phone")
                    break
                
            
            if phone_address == None:
                print("Phone not found, retrying...")
            else:
                break          

           
    except Exception as err:
         print(err)


def start():
    port = 1
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.connect((phone_address,port))
    server_socket.listen(1)
    client_socket,address = server_socket.accept()
    data = client_socket.recv(1024)
    print(str(data))
    client_socket.close()
    server_socket.close()

def stop():
    try:
	None
    except Exception:
	raise Exception("unable to stop")