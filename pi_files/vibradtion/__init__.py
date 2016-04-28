__author__ = 'James'
import  winsound
import threading
import os
if os.name='posix':
	import ossaudiodev;

class start(threading.Thread):
	def __init__():
		super(start,self).__init__()
	
	def run(self):
		winsound.PlaySound("launch bass boost long.wav", winsound.SND_FILENAME)
	

def setup():
    try:
		
        return True
    except Exception:
        raise Exception("unable to set up")
        return False


def stop():
	
    try:
        return True
    except Exception:
        return False

