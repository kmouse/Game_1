import pygame
import sys
from load import get_font
from button import Button

screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

buttons = pygame.sprite.Group()
Button.containers = buttons
Button(screen, "Press", "", "width/2", "height/2")

font = pygame.font.Font(get_font('arial.ttf'), 20)
font_surface = font.render("Insanity is doing the same thing over and", 1, (0, 0, 0))
font_surface2 = font.render("over again, and expecting a different result.", 1, (0, 0, 0))
    
    
while True:
    screen.fill((245, 223, 79))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for button in buttons:
        button.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed(), screen)
    buttons.draw(screen)
    screen.blit(font_surface, (screen.get_width() / 2 - font_surface.get_width() / 2, 30))
    screen.blit(font_surface2, (screen.get_width() / 2 - font_surface2.get_width() / 2, 60))
    pygame.display.update()