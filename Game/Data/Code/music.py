import pygame, random
from load import get_music, list_music

class Music:
    def __init__(self, location):
        self.location = location
        self.songs = list_music(location)
        self.song = ""
        
    def play_music(self):
        if not pygame.mixer.music.get_busy():
            self.song = random.choice(self.songs)
            print(self.song)
            pygame.mixer.music.load(get_music(self.location + "\\" + self.song))
            pygame.mixer.music.play()
            
    def stop_music(self):
        pygame.mixer.music.fadeout(2000)