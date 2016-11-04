__author__ = 'James Dewes'


class wind:
    def __int__(self, pin):
        self.pin = pin
        try:
            import RPi.GPIO as GPIO
        except RuntimeError:
            print("Unable to import GPIO")
            raise Exception("Unable to import GPIO")

        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            #21 is not used by the PyGlow on the Pi  B
            GPIO.setup(self.pin, GPIO.OUT)
        except Exception as error:
            print(error)
            raise Exception("unable to set up" + repr(error))

    def start(self):
        #start the fan
        try:
            GPIO.output(self.pin, 1)
        except:
            raise Exception("unable to start")


    def stop(self):
        #stop the fan
        try:
            GPIO.output(self.pin, 0)
            GPIO.cleanup()
        except:
            raise Exception("unable to stop")

