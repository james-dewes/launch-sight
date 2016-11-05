class Bass:
    __author__ = 'James Dewes'

    def __init__(self):
        try:
            import pygame.mixer
            from pygame.mixer import Sound
        except RuntimeError:
            print("Unable to import pygame mixer sound")
            raise Exception("Unable to import pygame mixer sound")

        self.soundfile = "launch_bass_boost_long.wav"
        self.mixer = pygame.mixer.init() #instance of pygame
        self.bass = Sound(self.soundfile)

    def start(self):
        state = self.bass.play()
        while state.get_busy() == True:
            continue

    def stop(self):
        try:
            Pass
        except Exception:
            raise Exception("unable to stop")
