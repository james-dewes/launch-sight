class bass:
    __author__ = 'James Dewes'
    def __init__(self):
        try:
            from pygame.mixer import Sound
        except RuntimeError:
            print("Unable to import pygame mixer sound")
            raise Exception("Unable to import pygame mixer sound")

        self.soundfile = "launch_bass_boost_long.wav"
        self.mixer = pygame.mixer.init() #instance of pygame
        self.bass = Sound(soundfile)

    def start(self):
        state = bass.play()
        while state.get_busy() == True:
            continue

    def stop(self):
        try:
            Pass
        except Exception:
            raise Exception("unable to stop")
