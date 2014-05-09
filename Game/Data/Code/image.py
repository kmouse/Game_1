import pygame
from load import get_image

# This is the base class for any button object
class Image(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width=64, height=20, image="button.png"):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image a blank sprite
        self.image = pygame.image.load(get_image(image)).convert_alpha()
        
        # Set up the rect for drawing
        self.rect = self.image.get_rect()
        self.rect.center = eval(x, {"width":screen.get_width()}), eval(y, {"height":screen.get_height()})
        
        # Stores the equations for positions
        self.position_formula = x, y
        
    # Get the pos for the new screen size
    def update_pos(self, screen):
        self.rect.center = eval(self.position_formula[0], {"width":screen.get_width()}), eval(self.position_formula[1], {"height":screen.get_height()})
        
    def update(self, mouse_pos, mouse_down, screen):
        return False