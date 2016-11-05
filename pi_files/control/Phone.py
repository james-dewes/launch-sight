class Phone:
    __author__ = 'James Dewes'
    def __init__(self, phone = "Nexus 5"):
        try:
            import bluetooth
            self.bluetooth  = bluetooth
        except RuntimeError:
            print("Unable to import bluetooth")
            raise Exception("Unable to import bluetooth")

        self.phone_address = None
        self.phone_name = phone
        for retry in range(0,5):
            self.nearby_devices = self.bluetooth.discover_devices()
            for bdaddr in self.nearby_devices:
                if self.phone_name == self.bluetooth.lookup_name(bdaddr):
                    self.phone_address = bdaddr
                    print("found phone")
                    break


            if self.phone_address == None:
                print("Phone not found, retrying...")
            else:
                break

    def start(self):
        port = 1
        self.server_socket = self.bluetooth.BluetoothSocket(self.bluetooth.RFCOMM)
        self.server_socket.connect((self.phone_address, port))
        self.server_socket.listen(1)
        self.client_socket.address = self.server_socket.accept()
        self.data = self.client_socket.recv(1024)
        print(str(data))
        self.client_socket.close()
        self.server_socket.close()

    def stop(self):
        try:
            Pass
        except Exception:
            raise Exception("unable to stop")
