import pygame
from button import Button
from image import Image

REDUCE_NUMBER_CODE = """if self.value > 0:
    self.plain_image = pygame.image.load(self.image_locations[0]).convert_alpha()
    self.highlight_image = pygame.image.load(self.image_locations[1]).convert_alpha()
    self.pressed_image = pygame.image.load(self.image_locations[2]).convert_alpha()
    font = pygame.font.Font(get_font('arial.ttf'), self.text_size)
    self.value -= 1
    font_surface = font.render(str(self.value) + " x", 1, (0, 0, 0))
    font_size = font.size(str(self.value) + " x")
    if self.text_align == "center":
        self.plain_image.blit(font_surface, (self.image.get_width() / 2 - font_size[0] / 2, self.image.get_height() / 2 - font_size[1] / 2))
        self.highlight_image.blit(font_surface, (self.image.get_width() / 2 - font_size[0] / 2, self.image.get_height() / 2 - font_size[1] / 2))
        self.pressed_image.blit(font_surface, (self.image.get_width() / 2 - font_size[0] / 2, self.image.get_height() / 2 - font_size[1] / 2))
    elif self.text_align == "left":
        self.plain_image.blit(font_surface, (20, self.image.get_height() / 2 - font_size[1] / 2))
        self.highlight_image.blit(font_surface, (20, self.image.get_height() / 2 - font_size[1] / 2))
        self.pressed_image.blit(font_surface, (20, self.image.get_height() / 2 - font_size[1] / 2))
else:
    self.value -= 1"""
    
    
    
class side_menu(pygame.sprite.Sprite):
    def __init__(self, screen, items):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.Surface((200, screen.get_height()))
        
        # Set up the rect for drawing
        self.rect = self.image.get_rect()
        self.rect.topright = (screen.get_width(), 0)
        
        # Set up the button and image containers
        self.static_items = pygame.sprite.Group()
        Button.containers = self.static_items
        Image.containers = self.static_items
        
        self.commands = []
    
        # Set up the buttons that have been loaded from file
        pos_y = 50
        increment = 90
        self.buttons = []
        # Go through each of the items and create a button for it
        for item in items:
            item = item.split(":")
            print(item)
            if item[0] == "Black Hole":
                self.buttons.append(Button(self.image, item[1] + " x", REDUCE_NUMBER_CODE, "width/2", str(pos_y), init_command="self.value=" + item[1], type="Create Black Hole",    image="Buttons\\Gameplay_Buttons\\black_hole_button.png", highlight_image="Buttons\\Gameplay_Buttons\\black_hole_button_highlighted.png", pressed_image="Buttons\\Gameplay_Buttons\\black_hole_button_pressed.png", text_align="left", press_method="mouse down"))
            elif item[0] == "Trigger Left":
                self.buttons.append(Button(self.image, item[1] + " x", REDUCE_NUMBER_CODE, "width/2", str(pos_y), init_command="self.value=" + item[1], type="Create Trigger Left",image="Buttons\\Gameplay_Buttons\\trigger_left_button.png", highlight_image="Buttons\\Gameplay_Buttons\\trigger_left_button_highlighted.png", pressed_image="Buttons\\Gameplay_Buttons\\trigger_left_button_pressed.png", text_align="left", press_method="mouse down"))
            elif item[0] == "Trigger Right":
                self.buttons.append(Button(self.image, item[1] + " x", REDUCE_NUMBER_CODE, "width/2", str(pos_y), init_command="self.value=" + item[1], type="Create Trigger Right",image="Buttons\\Gameplay_Buttons\\trigger_right_button.png", highlight_image="Buttons\\Gameplay_Buttons\\trigger_right_button_highlighted.png", pressed_image="Buttons\\Gameplay_Buttons\\trigger_right_button_pressed.png", text_align="left", press_method="mouse down"))
        
            pos_y += increment
        
        
        # Create the default menu buttons
        self.buttons.append(Button(self.image, "Menu", "print('Menu')", "50", "height-30", image="Buttons\\small_button-white.png", highlight_image="Buttons\\small_button_highlighted-white.png", pressed_image="Buttons\\small_button_pressed-white.png", text_size=20))
        
        self.buttons.append(Button(self.image, "Options", "print('Options')", "width-50", "height-30", image="Buttons\\small_button-white.png", highlight_image="Buttons\\small_button_highlighted-white.png", pressed_image="Buttons\\small_button_pressed-white.png", text_size=20))
        
        # Game control buttons
        self.buttons.append(Button(self.image, "Play", "print('Play')", "50", "height-100", image="Buttons\\small_button-white.png", highlight_image="Buttons\\small_button_highlighted-white.png", pressed_image="Buttons\\small_button_pressed-white.png", text_size=20, init_command="self.value=1", type="play game"))
        
        self.buttons.append(Button(self.image, "Restart", "print('Restart')", "width-50", "height-100", image="Buttons\\small_button-white.png", highlight_image="Buttons\\small_button_highlighted-white.png", pressed_image="Buttons\\small_button_pressed-white.png", text_size=20, init_command="self.value=1", type="restart game"))
        
        
        # Create the menu break for asthetic reasons
        Image(self.image, "width/2", "height-65", image="Static_Images\\break.png")
        
    def update_pos(self, screen):
         # Remake the image
        self.image = pygame.Surface((200, screen.get_height()))
        
        # Set up the rect for drawing
        self.rect = self.image.get_rect()
        self.rect.topright = (screen.get_width(), 0)
        
        for item in self.static_items:
            item.update_pos(self.image)
        
    def update(self, screen):
        self.image.fill((30, 133, 145))
        x, y = pygame.mouse.get_pos()
        for item in self.static_items:
            pressed = item.update((x - (screen.get_width() - 200), y), pygame.mouse.get_pressed(), self.image)
            if pressed and hasattr(item, "value") and item.value >= 0:
                print("aaa")
                self.commands.append(item.type)
        self.static_items.draw(self.image)