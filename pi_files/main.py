'''launch sight code for raspberry pi'''
def main():
    import fx, control, time
    
    #set up the effects (go, no-go list)
    
    try:
        wind = fx.Wind()
        wind_state = "go"
        print("wind go")
    except:
        wind_state = "no-go"
        print("wind no-go")

    try:
        rumble = fx.Rumble()
        rumble_state = "go"
        print("rumble go")
    except:
        rumble_state = "no-go"
        print("rumble no-go")

    try:
         bass = fx.Bass()
         print("bass go")
         bass_state = "go"
    except:
        bass_state = "no-go"
        print("bass no-go")

    ##run the effects
    if wind_state == "go":
        wind.start()
    if rumble_state == "go":
        rumble.start()
    if bass_state == "go":
        bass.start()

    #just for testing
    time.sleep(20)

    ##stop the effects
    if wind_state == "go":
        wind.stop()
    if rumble_state == "go":
        rumble.stopt()
    if bass_state == "go":
        bass.stop()


if __name__ == '__main__':main()
