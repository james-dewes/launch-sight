'''launch sight code for raspberry pi'''
def main():
    import time
    import wind
    import bass
    import lights
    import rumble
    import phone
    
    #reset the lights
    lights.reset()

    #set up the control
    lights.stop()

    #set up the effects
    lights.warn()
    try:
        wind.setup()
        wind_state = "go"
    except:
        lights.stop()    
        wind_state = "no-go"

    lights.warn()
    try:
        rumble.setup()
        rumble_state = "go"
    except:
        lights.stop()
        rumble_state = "no-go"

    lights.warn()
    try:
         bass.setup()
         bass_state = "go"
    except:
         lights.stop()
	 bass_state = "no-go"

    ##run the effects
    lights.go()
    time.sleep(20)
    lights.launch()
    if wind_state == "go":wind.start()
    if rumble_state == "go":rumble.start()
    if bass_state == "go":bass.start()
    #just for testing
    time.sleep(20)

    ##stop the effects
    lights.reset()
    if wind_state == "go":wind.stop()
    if rumble_state == "go":rumble.stopt()
    if bass_state == "go": bass.stop()


if __name__ == '__main__':main()
