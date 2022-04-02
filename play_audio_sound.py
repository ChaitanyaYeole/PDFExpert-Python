# import pygame
# pygame.mixer.init()

# def read(file_path):
#     outfile = "cache/temp.mp3"
#     pygame.mixer.music.load(outfile)
#     pygame.mixer.music.play()

# def stop():
#     pygame.mixer.music.stop()

# def pause():
#     pygame.mixer.music.pause()

# def unpause():
#     pygame.mixer.music.unpause()

import pyttsx3
import pygame

pygame.mixer.init()
engine = pyttsx3.init()



def read(text):
    outfile = "cache/temp.wav"
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 150)
    engine.setProperty("voice", voices[1].id)
    engine.save_to_file(text, outfile)
    engine.runAndWait()
    pygame.mixer.music.load(outfile)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()
