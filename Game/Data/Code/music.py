import pygame, random
from load import get_music, list_music

class Music:
    def __init__(self, location):
        self.location = location
        self.songs = list_music(location)
        self.song = ""
        self.play = True
        
    def play_music(self):
        if not pygame.mixer.music.get_busy() and self.play:
            self.song = random.choice(self.songs)
            print(self.song)
            pygame.mixer.music.load(get_music(self.location + "\\" + self.song))
            pygame.mixer.music.play()
            
    def stop_music(self):
        pygame.mixer.music.fadeout(2000)
        
    def skip(self):
        self.song = random.choice(self.songs)
        print(self.song)
        pygame.mixer.music.load(get_music(self.location + "\\" + self.song))
        if self.play:
            pygame.mixer.music.play()
        
    def play_pause(self):
        if self.play:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.play = not self.play