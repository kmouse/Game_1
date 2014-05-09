import pygame
from load import get_image

class Cutscene:
    def __init__(self, screen, image):
        self.image = pygame.image.load(get_image(image)).convert_alpha()
        if screen.get_width() > screen.get_height():
            width = int(screen.get_height() / self.image.get_height() * self.image.get_width())
            height = int(screen.get_height())
            self.image = pygame.transform.scale(self.image, (width, height))
        elif screen.get_width() < screen.get_height():
            pass
        else:
            pass