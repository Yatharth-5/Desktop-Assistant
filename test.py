import pygame
from pygame import mixer
from playsound import playsound
import datetime
import time

def playmusic(song):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)
    time.sleep(4)

playmusic("shubhshubh.mp3")