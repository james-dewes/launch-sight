__author__ = 'James Dewes'


class lights:
    def __ini__(self):
        slef.brightness = 50
        try:
            import piglow

        except RuntimeError:
            print("Unable to inport piglow")
            raise Exception("Unable to inport piglow")

        from time import sleep
        piglow.auto_update = True

        def cycle(self):
            while 1:
                piglow.arm1(slef.brightness)
                sleep(1)
                piglow.arm2(slef.brightness)
                piglow.arm1(0)
                sleep(1)
                piglow.arm2(0)
                piglow.arm3(slef.brightness)
                sleep(1)
                piglow.arm3(0)

        def reset(self):
            piglow.all(0)
            piglow.set(range(1,17),0)

        def stop(self):
            piglow.all(0)
            piglow.set(range(1,17),0)
            piglow.red(slef.brightness)

        def warn(self):
            piglow.all(0)
            piglow.set(range(1,17),0)
            piglow.yellow(slef.brightness)

        def go(self):
            piglow.all(0)
            piglow.set(range(1,17),0)
            piglow.green(slef.brightness)

        def launch(self):
            for i in range(0,-5,-1):
                piglow.set([i,i+6,i+i+12],60)
                sleep(3)




