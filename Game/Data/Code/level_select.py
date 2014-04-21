import pygame
from button import Button

BACKGROUND_COLOR = (15, 24, 122)

# The distance between buttons
DIST = 140

class Level_Select:
    """This class controls all the level select buttons and screen design and arrangement as well as handling mouse events for the buttons"""
    def __init__(self, screen, levels, unlocked):
        """Create and place all the buttons in correct positions"""
        self.update_pos(screen, levels, unlocked)
        
    def update(self, mouse_pos, mouse_pressed):
        """Draw the buttons and update states. If one button is pressed return the level."""
        self.image.fill(BACKGROUND_COLOR)
        for item in self.buttons:
            if item.update(mouse_pos, mouse_pressed, self.image):
                return item.level
            
            
        self.buttons.draw(self.image)
        return 0
        
    def update_pos(self, screen, levels, unlocked):
        """Create and place all the buttons in correct positions"""
        
        # Current x and y positions
        x = 80
        y = 200
        
        # The screen that the buttons draw on 
        self.image = pygame.Surface(screen.get_size())
        
        # The sprite group that controls the buttons
        self.buttons = pygame.sprite.Group()
        Button.containers = self.buttons
        
        # Go along and place the buttons right to left, top to bottom, leaving DIST distance between them
        for item in range(levels):
            if item + 1 <= unlocked:
                if x <= screen.get_width() - 80 and x >= 80:
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(item + 1),
                    image="Buttons\\level_button.png", highlight_image="Buttons\\level_button_highlighted.png", pressed_image="Buttons\\level_button_pressed.png", text_align="left")
                else:
                    x = 80
                    y += DIST
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(item + 1),
                    image="Buttons\\level_button.png", highlight_image="Buttons\\level_button_highlighted.png", pressed_image="Buttons\\level_button_pressed.png", text_align="left")
                    
            else:
                if x <= screen.get_width() - 80 and x >= 80:
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(0),
                    image="Buttons\\level_button-grey.png", highlight_image="Buttons\\level_button-grey.png", pressed_image="Buttons\\level_button-grey.png", text_align="left")
                else:
                    x = 80
                    y += DIST
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(0),
                    image="Buttons\\level_button-grey.png", highlight_image="Buttons\\level_button-grey.png", pressed_image="Buttons\\level_button-grey.png", text_align="left")
                
            x += DIST