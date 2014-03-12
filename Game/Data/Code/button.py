import pygame
import os
from load import get_image, get_font

pygame.init()

# This is the base class for any button object
class Button(pygame.sprite.Sprite):
    def __init__(self, screen, text, command, x, y, width=64, height=20, image="Buttons\\button.png", highlight_image="Buttons\\button_highlighted.png", pressed_image="Buttons\\button_pressed.png", init_command="", text_size=24, text_align="center", type="Button", press_method="click"):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.image.load(get_image(image)).convert_alpha()
        
        # Set up the rect for drawing
        self.rect = self.image.get_rect()
        self.rect.center = eval(x, {"width":screen.get_width()}), eval(y, {"height":screen.get_height()})
        
        # Stores the equations for positions
        self.position_formula = x, y
        
        # Store the images
        self.plain_image = pygame.image.load(get_image(image)).convert_alpha()
        self.highlight_image = pygame.image.load(get_image(highlight_image)).convert_alpha()
        self.pressed_image = pygame.image.load(get_image(pressed_image)).convert_alpha()
        
        # This gets whether the mouse pressed self
        self.pressed = 0
        
        self.text_size = text_size
        self.text = text
        self.text_align = text_align
        self.image_locations = [get_image(image), get_image(highlight_image), get_image(pressed_image)]
        self.type = type
        
        font = pygame.font.Font(get_font('arial.ttf'), text_size)
        font_surface = font.render(text, 1, (0, 0, 0))
        font_size = font.size(text)
        if text_align == "center":
            self.plain_image.blit(font_surface, (self.image.get_width() / 2 - font_size[0] / 2, self.image.get_height() / 2 - font_size[1] / 2))
            self.highlight_image.blit(font_surface, (self.image.get_width() / 2 - font_size[0] / 2, self.image.get_height() / 2 - font_size[1] / 2))
            self.pressed_image.blit(font_surface, (self.image.get_width() / 2 - font_size[0] / 2, self.image.get_height() / 2 - font_size[1] / 2))
        elif text_align == "left":
            self.plain_image.blit(font_surface, (20, self.image.get_height() / 2 - font_size[1] / 2))
            self.highlight_image.blit(font_surface, (20, self.image.get_height() / 2 - font_size[1] / 2))
            self.pressed_image.blit(font_surface, (20, self.image.get_height() / 2 - font_size[1] / 2))
            
        # This is the command run when the button is pressed
        self.command = command
        self.init_command = init_command
        
        self.press_method = press_method
        
        # Run the init_command
        self.run_init_command()
        
    # Get the pos for the new screen size
    def update_pos(self, screen):
        self.rect.center = eval(self.position_formula[0], {"width":screen.get_width()}), eval(self.position_formula[1], {"height":screen.get_height()})
        
    def update(self, mouse_pos, mouse_down, screen):
        pressed = False
        mouse_rect = pygame.Rect(mouse_pos, (1, 1))
        # If the mouse is on the button
        # When self.pressed == 1 then the mouse is down and started over the button
        # When self.pressed == 0 then the mouse is not down
        # When self.pressed == 2 then the mouse is down but did not start over the button or button is already used
        
        if self.rect.colliderect(mouse_rect):
            if mouse_down[0] and self.pressed == 0:
                self.pressed = 1
                self.image = self.pressed_image
            elif mouse_down[0] and self.pressed == 1:
                self.pressed = 1
                if self.press_method == "mouse down": self.run_command(); self.pressed = 2; pressed = True
                self.image = self.pressed_image
            elif mouse_down[0] and self.pressed == 2:
                self.pressed = 2
            else:
                if self.pressed == 1:
                    if self.press_method == "click": self.run_command()
                    pressed = True
                self.pressed = 0
                self.image = self.highlight_image
        else:
            if mouse_down[0] and self.pressed == 0:
                self.pressed = 2
            elif mouse_down[0] and self.pressed == 1:
                self.pressed = 1
            elif mouse_down[0] and self.pressed == 2:
                self.pressed = 2
            else:
                self.pressed = 0
            self.image = self.plain_image
        
        # Update rect
        self.rect = self.image.get_rect()
        self.update_pos(screen)
        
        return pressed
        
    def run_init_command(self):
        exec(self.init_command)
        
    def run_command(self):
        exec(self.command)