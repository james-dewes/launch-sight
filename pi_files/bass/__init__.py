__author__ = 'James'
import pygame
from pygame.mixer import Sound
soundfile = "launch_bass_boost_long.wav"
bass = None
def setup():
    try:
        global bass
        pygame.mixer.init()
        bass = Sound(soundfile)
    except Exception:
        raise Exception("unable to set up")

def start():
    state = bass.play()
    while state.get_busy() == True:
        continue    

def stop():
    try:
	None
    except Exception:
	raise Exception("unable to stop")
