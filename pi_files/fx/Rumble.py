class Rumble:
    __author__ = 'James Dewes'
    def __init__(self):
        try:
            import bluetooth
            self.bluetooth = bluetooth
        except RuntimeError:
            print("Unable to import blutooth. bluetooth module not installed?")
            raise Exception("Unable to import blutooth. bluetooth module not installed?")

        self.rumble_pack_address = None
        self.server_socket = None
        self.rumble_pack_name = "HC-05"
        try:
            flag = 0
            for retry in range(0, 5):
                self.nearby_devices = self.bluetooth.discover_devices()
                for bdaddr in self.nearby_devices:
                    if self.rumble_pack_name == self.bluetooth.lookup_name(bdaddr):
                        self.rumble_pack_address = bdaddr
                        print("found rumble_pack")
                        break
                    if self.rumble_pack_address == None:
                        print("rumble_pack not found, retrying...")
                    else:
                        break

        except Exception as err:
            print(err)

    def start(self):
        port = 1
        self.server_socket = self.bluetooth.BluetoothSocket(self.bluetooth.RFCOMM)
        self.server_socket.connect((self.rumble_pack_address,port))
        self.server_socket.send("1")

    def stop(self):
        try:
            self.server_socket.close()
        except Exception:
            raise Exception("unable to stop")
