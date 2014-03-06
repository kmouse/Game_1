import pygame, random
from load import get_music, list_music

class Music:
    def __init__(self, location):
        self.location = location
        self.songs = list_music(location)
        
    def play_music(self):
        if not pygame.mixer.music.get_busy():
            song = random.choice(self.songs)
            pygame.mixer.music.load(get_music(self.location + "\\" + song))
            print(song)
            pygame.mixer.music.play()
            
    def stop_music(self):
        pygame.mixer.music.fadeout(2000)