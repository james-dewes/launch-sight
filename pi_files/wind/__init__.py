__author__ = 'James'
import RPi.GPIO as gpio
def setup():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #21 is not used by the PyGlow on the Pi  B
        GPIO.setup(21, GPIO.OUT)
        return True
    except Exception:
        raise Exception("unable to set up")
        return False


def start():
    #start the fan
    try:
        GPIO.output(port_or_pin, 1)
        return True
    except Exception:
        raise Exception("unable to start")
        return False

def stop():
    #stop the fan
    try:
        GPIO.output(port_or_pin, 0)
        return True
    except Exception:
        raise Exception("unable to stop")
        return False

