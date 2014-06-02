import pygame
from Data.Code.load import get_image

# This is the base class for any button object
class Image(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, width=0, height=0, image="button.png"):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image a blank sprite
        self.image = pygame.image.load(get_image(image)).convert_alpha()
        
        # Set up the rect for drawing
        # if the width or height is 0, that is the default width or height for the image
        if width == 0:
            rect_width = self.image.get_width()
        else:
            rect_width = width
        
        if height == 0:
            rect_height = self.image.get_height()
        else:
            rect_height = height
            
        self.rect = pygame.Rect(0, 0, rect_width, rect_height)
        self.rect.center = eval(x, {"width":screen.get_width()}), eval(y, {"height":screen.get_height()})
        
        # Stores the equations for positions
        self.position_formula = x, y
        
    # Get the pos for the new screen size
    def update_pos(self, screen):
        self.rect.center = eval(self.position_formula[0], {"width":screen.get_width()}), eval(self.position_formula[1], {"height":screen.get_height()})
        
    def update(self, mouse_pos, mouse_down, screen):
        return False