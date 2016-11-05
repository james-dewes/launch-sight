__author__ = 'James Dewes'


class Phone:
    def __init__(self, phone = "Nexus 5"):
        try:
            import bluetooth
        except RuntimeError:
            print("Unable to import bluetooth")
            raise Exception("Unable to import bluetooth")

        self.phone_address = None
        self.phone_name = phone
        for retry in range(0,5):
            nearby_devices = bluetooth.discover_devices()
            for bdaddr in nearby_devices:
                if self.phone_name == bluetooth.lookup_name(bdaddr):
                    self.phone_address = bdaddr
                    print("found phone")
                    break


            if self.phone_address == None:
                print("Phone not found, retrying...")
            else:
                break

    def start(self):
        port = 1
        server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_socket.connect((self.phone_address, port))
        server_socket.listen(1)
        client_socket.address = server_socket.accept()
        data = client_socket.recv(1024)
        print(str(data))
        client_socket.close()
        server_socket.close()

    def stop(self):
        try:
            Pass
        except Exception:
            raise Exception("unable to stop")