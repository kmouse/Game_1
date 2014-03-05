import pygame
from load import get_image

class Black_Hole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.image.load(get_image("Gameplay_Objects\\black_hole.png"))
        
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        
        self.mass = 5
        
        self.x = x
        self.y = y
        
        self.move = True
        
    def update(self, mouse_pos, mouse_pressed, offset):
        if mouse_pressed[0]:
            if self.move:
                self.x, self.y = mouse_pos[0] + offset[0], mouse_pos[1] + offset[1]
                self.rect.center = self.x, self.y
        else:
            self.move = False
        

        
        
class Trigger_Left(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
         # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        
        pygame.draw.rect(self.image, (255, 80, 21), self.image.get_rect(), 3)
        
        left_arrow = pygame.image.load(get_image("Gameplay_Objects\\left_arrow.png"))
        
        self.image.blit(left_arrow, (width / 2 - left_arrow.get_width() / 2, height / 2 - left_arrow.get_height() / 2))
        
        self.rect = pygame.Rect((x, y), (width, height))
        
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height
        
        self.move = True
        
    def update(self, mouse_pos, mouse_pressed, offset):
        if mouse_pressed[0]:
            if self.move:
                self.x, self.y = mouse_pos[0] + offset[0], mouse_pos[1] + offset[1]
                self.rect.center = self.x, self.y
        else:
            self.move = False
        
        
        
        
class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
         # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        
        pygame.draw.rect(self.image, (100, 255, 30), self.image.get_rect(), 3)
        
        self.rect = pygame.Rect((x, y), (width, height))
        
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height
        
    def update(self, mouse_pos, mouse_pressed, offset):
        pass