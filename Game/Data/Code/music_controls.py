BLUE = (30, 133, 145)
from button import Button

class Music_Controls(pygame.sprite.Sprite):
    def __init__(self, location):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        # Make the image
        self.image = pygame.Surface((100, 50))
        
        self.image.fill(BLUE)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, 50)
        
        self.buttons = []
        buttons = pygame.sprite.Group()
        Button.containers = buttons
        
        self.buttons.append(Button(self.image, "", "", "width/4", "height/2"))
        self.buttons.append(Button(self.image, "", "", "width*3/4", "height/2"))