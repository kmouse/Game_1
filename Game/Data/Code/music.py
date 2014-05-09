import pygame, random
from load import get_music, list_music
import logging

# Log debug and higher calls to this file
logging.basicConfig(filename='game.log', level=logging.DEBUG)

class Music:
    def __init__(self, location):
        logging.debug("Music initialising")
        self.location = location
        self.songs = list_music(location)
        self.song = ""
        self.play = True
        
    def play_music(self):
        if not pygame.mixer.music.get_busy() and self.play:
            self.song = random.choice(self.songs)
            logging.info("Music playing: " + self.song)
            pygame.mixer.music.load(get_music(self.location + "\\" + self.song))
            pygame.mixer.music.play()
            
    def stop_music(self):
        logging.debug("Fading music")
        pygame.mixer.music.fadeout(2000)
        
    def skip(self):
        logging.debug("Skipping music")
        self.song = random.choice(self.songs)
        logging.info("Music playing: " + self.song)
        pygame.mixer.music.load(get_music(self.location + "\\" + self.song))
        if self.play:
            pygame.mixer.music.play()
        
    def play_pause(self):
        if self.play:
            logging.info("Pausing music")
            pygame.mixer.music.pause()
        else:
            logging.info("Unpausing music")
            pygame.mixer.music.unpause()
        self.play = not self.play