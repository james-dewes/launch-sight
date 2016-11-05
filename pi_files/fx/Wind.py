#!/usr/bin/python
# --------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#    Stepper Motor Test
#
# A simple script to control
# a stepper motor.
#
# Author : Matt Hawkins
# Date   : 28/09/2015
# Modified: James Dewes
# Date   : 05/11/2016
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------
class Wind:
    def ___init__(self):
        # Import required libraries
        import time
        self.time = time
        import RPi.GPIO as GPIO

        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)

        # GPIO17,GPIO22,GPIO23,GPIO24
        StepPins = [17, 22, 23, 24]

        # Set all pins as output
        for pin in StepPins:
            self.GPIO.setup(pin, self.GPIO.OUT)
            self.GPIO.output(pin, False)

        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.Seq = [[1, 0, 0, 1],
                    [1, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 1],
                    [0, 0, 0, 1]]

        self.StepCount = len(Seq)
        self.WaitTime = 10 / float(1000)


def start(self, StepDir=1):  # Start main loop
    StepCounter = 0
    while True:
        for pin in range(0, 4):
            xpin = selfStepPins[pin]
            if self.Seq[StepCounter][pin] != 0:
                self.GPIO.output(xpin, True)
            else:
                self.GPIO.output(xpin, False)
                self.StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (StepCounter >= StepCount):
            StepCounter = 0
        if (StepCounter < 0):
            StepCounter = self.StepCount + StepDir

        self.time.sleep(WaitTime)