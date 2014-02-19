import pygame
from load import get_image

class Black_Hole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.image.load(get_image("black_hole.png"))
        
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        
        self.mass = 20