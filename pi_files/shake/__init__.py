__author__ = 'James'
#control the rumble pack
import bluetooth
  

class start(threading.Thread):
	winsound.PlaySound("launch bass boost long.wav", winsound.SND_FILENAME)
	

def setup():
    try:
		rumble_pack_name ="HC-05"
		rumble_pack_address = None
		nearby_devices = bluetooth.discover_devices()
		##find device addresses
		for bdaddr in nearby_devices:
			if rumble_pack_name == bluetooth.lookup_name( bdaddr ):
				rumble_pack_address = bdaddr
				return True
			
		
	
    except Exception:
        raise Exception("unable to set up")
        return False


def stop():
	
    try:
        return True
    except Exception:
        return False

