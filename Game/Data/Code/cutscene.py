import pygame
from Data.Code.load import get_image

class Cutscene:
    def __init__(self, screen, image):
        image = "Static_Images/Cutscenes/" + image
        self.image = pygame.image.load(get_image(image)).convert_alpha()
        if screen.get_width() > screen.get_height():
            width = int(screen.get_height() / self.image.get_height() * self.image.get_width())
            height = int(screen.get_height())
            self.image = pygame.transform.scale(self.image, (width, height))
            
        # If the window is taller than it is wide
        # Resize the cutscene so it fits horizontally
        elif screen.get_width() < screen.get_height():
            width = int(screen.get_width())
            height = int(screen.get_width() / self.image.get_width() * screen.get_height())
            self.image = pygame.transform.scale(self.image, (width, height))
        else:
            width = int(screen.get_width())
            height = int(screen.get_height())
            self.image = pygame.transform.scale(self.image, (width, height))