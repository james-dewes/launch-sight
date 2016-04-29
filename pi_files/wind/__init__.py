__author__ = 'James'
import RPi.GPIO as GPIO
def setup():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        #21 is not used by the PyGlow on the Pi  B
        GPIO.setup(21, GPIO.OUT)
        return True
    except Exception as error:
        print(error)
        #raise Exception("unable to set up" + repr(error))
        return False


def start():
    #start the fan
    try:
        GPIO.output(21, 1)
        return True
    except:
        raise Exception("unable to start")
        return False

def stop():
    #stop the fan
    try:
        GPIO.output(21, 0)
        GPIO.cleanup()
        return True
    except:
        raise Exception("unable to stop")
        return False

