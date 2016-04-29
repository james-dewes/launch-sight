__author__ = 'James'
import piglow
from time import sleep
piglow.auto_update = True
def cycle():
    while 1:
        piglow.arm1(50)
        sleep(1)
        piglow.arm2(50)
        piglow.arm1(0)
        sleep(1)
        piglow.arm2(0)
        piglow.arm3(50)
        sleep(1)
        piglow.arm3(0)

def reset():
    piglow.all(0)
    piglow.set(range(1,17),0)

def stop():
    piglow.all(0)
    piglow.set(range(1,17),0)
    piglow.red(50)

def warn():
    piglow.all(0)
    piglow.set(range(1,17),0)
    piglow.yellow(50)

def go():
    piglow.all(0)
    piglow.set(range(1,17),0)
    piglow.green(50)

def launch():
    for i in range(0,-5,-1):
        piglow.set([i,i+6,i+i+12],60)
        sleep(3)


        