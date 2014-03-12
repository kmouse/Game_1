BLUE = (30, 133, 145)
from button import Button
from music import Music
import pygame

PLAY_PAUSE_LOAD_IMAGES = """self.value = 1
self.images1 = (pygame.image.load(get_image("Buttons\\play_button.png")).convert_alpha(), pygame.image.load(get_image("Buttons\\play_button_highlighted.png")).convert_alpha(), pygame.image.load(get_image("Buttons\\play_button_pressed.png")).convert_alpha())

self.images2 = (pygame.image.load(get_image("Buttons\\pause_button.png")).convert_alpha(), pygame.image.load(get_image("Buttons\\pause_button_highlighted.png")).convert_alpha(), pygame.image.load(get_image("Buttons\\pause_button_pressed.png")).convert_alpha())"""

PLAY_PAUSE_SWAP_IMAGE = """print(self.value)
self.value = 1 if self.value == 0 else 0
print(self.value)
if self.value == 0:
    self.plain_image = self.images1[0]
    self.highlight_image = self.images1[1]
    self.pressed_image = self.images1[2]
elif self.value == 1:
    self.plain_image = self.images2[0]
    self.highlight_image = self.images2[1]
    self.pressed_image = self.images2[2]
self.image = self.plain_image
"""
    
class Music_Controls(pygame.sprite.Sprite):
    def __init__(self, location):
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        # Make the image
        self.image = pygame.Surface((120, 50))
        
        self.image.fill(BLUE)
        
        self.offset = (20, 20)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.offset
        
        self.buttons = []
        self.button_group = pygame.sprite.Group()
        Button.containers = self.button_group
        
        self.buttons.append(Button(self.image, "", PLAY_PAUSE_SWAP_IMAGE, "width/4", "height/2", image="Buttons\\pause_button.png", highlight_image="Buttons\\pause_button_highlighted.png", pressed_image="Buttons\\pause_button_pressed.png", type="play pause", init_command=PLAY_PAUSE_LOAD_IMAGES))
        self.buttons.append(Button(self.image, "", "", "width*3/4", "height/2", image="Buttons\\skip_forwards_button.png", highlight_image="Buttons\\skip_forwards_button_highlighted.png", pressed_image="Buttons//skip_forwards_button_pressed.png", type="skip"))
        
        self.button_group.draw(self.image)
        
        # Create music
        self.music = Music(location)
        self.music.play_music()
        
    def play_music(self, mouse_pos, mouse_down):
        self.image.fill(BLUE)
        mouse_pos = mouse_pos[0] - self.offset[0], mouse_pos[1] - self.offset[1]
        for item in self.buttons:
            pressed = item.update(mouse_pos, mouse_down, self.image)
            if pressed:
                if item.type == "skip":
                    self.music.skip()
                elif item.type == "play pause":
                    self.music.play_pause()
        self.button_group.draw(self.image)
        
        self.music.play_music()