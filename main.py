'''launch sight code for raspberry pi'''
def main:
	import RPi.GPIO as gpio
    import bluetooth
    import time
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
			
		if rumble_pack_name == bluetooth.lookup_name( bdaddr ):
			rumble_pack_address = bdaddr
			
		if controller_name == bluetooth.lookup_name( bdaddr ):
			controller_address = bdaddr
			
	
	#is the phone on and connected
	if phone_address != None:
		#start listening to the phone
		port = 3
		s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		s.connect((phone_address, port))

		while 1:
			text = raw_input()
			#some sort of exit code
			if text == "quit":
				s.send(text)
			    break
		    
			#Did the phone tell us to start?
			if text == "start":
			#send a message to the rumble pack
			port = 1
			sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
			sock.connect((rumble_pack_address, port))
			sock.send(1)
			sock.close()
			
			#start the fan
			GPIO.setmode(GPIO.BCM)
			GPIO.setwarnings(False)
			
			#play the base wav file
			
			#check if the phone told us to stop OR control stop
			if :
				#stop the fan
				#stop the base track
				
				#stop the rumble pack
				port = 1
				sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
				sock.connect((rumble_pack_address, port))
				sock.send(1)
				sock.close()
				
			
		
	else:
		#Flash red or something
		None
		
	
	
	
	
	
if __name__ == '__main__':main()
