import pygame
from button import Button

BACKGROUND_COLOR = (15, 24, 122)

class Level_Select:
    def __init__(self, screen, levels, unlocked):
        x = 80
        y = 200
        dist = 140
        
        self.image = pygame.Surface(screen.get_size())
        self.buttons = pygame.sprite.Group()
        Button.containers = self.buttons
        
        for item in range(levels):
            if item + 1 <= unlocked:
                if x <= screen.get_width() - 80 and x >= 80:
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(item + 1),
                    image="Buttons\\level_button.png", highlight_image="Buttons\\level_button_highlighted.png", pressed_image="Buttons\\level_button_pressed.png", text_align="left")
                else:
                    x = 80
                    y += dist
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(item + 1),
                    image="Buttons\\level_button.png", highlight_image="Buttons\\level_button_highlighted.png", pressed_image="Buttons\\level_button_pressed.png", text_align="left")
                    
            else:
                if x <= screen.get_width() - 80 and x >= 80:
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(0),
                    image="Buttons\\level_button-grey.png", highlight_image="Buttons\\level_button-grey.png", pressed_image="Buttons\\level_button-grey.png", text_align="left")
                else:
                    x = 80
                    y += dist
                    Button(self.image, "Level" + str(item + 1), "", str(x), str(y), init_command="self.level=" + str(0),
                    image="Buttons\\level_button-grey.png", highlight_image="Buttons\\level_button-grey.png", pressed_image="Buttons\\level_button-grey.png", text_align="left")
                
            x += dist
        self.buttons.draw(self.image)
        
    def update(self, mouse_pos, mouse_pressed):
        self.image.fill(BACKGROUND_COLOR)
        for item in self.buttons:
            if item.update(mouse_pos, mouse_pressed, self.image):
                return item.level
            
            
        self.buttons.draw(self.image)
        return 0
        
    def update_pos(self, screen, levels, unlocked):
        self.__init__(screen, levels, unlocked)