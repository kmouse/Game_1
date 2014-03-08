from button import Button
from image import Image
from mouse import Mouse
from music import Music
import pygame
import sys

BACKGROUND = (239, 255, 168)
BLACK = (25, 25, 25)
WHITE = (225, 225, 225)


def run_menu():
    # Initialise pygame modules
    pygame.init()
    
    music = Music("Menu")
    music.play_music()
    
    # Create screen with size (640, 480) and allow resizing
    screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
    
    # Hide the mouse
    pygame.mouse.set_visible(0)
    
    # Create a group to control and contain the button and image sprites
    static_items = pygame.sprite.Group()
    Button.containers = static_items
    Image.containers = static_items
    
    # Create the buttons
    start_button = Button(screen, "Start", "self.exit = True", "width/2", "((height - 220) / 8) * 1 + 220", init_command="self.exit = False")
    options_button = Button(screen, "Options", "print('1')", "width/2", "((height - 220) / 8) * 3 + 220")
    quit_button = Button(screen, "Quit", "import sys; sys.exit()", "width/2", "((height - 220) / 8) * 5 + 220")
    
    # Create the title
    Image(screen, "width/2", "120", image="Static_Images\\game_title.png")
    
    # This is used to cap the framerate
    clock = pygame.time.Clock()
    
    mouse = Mouse()
    
    # Run the menu
    while not start_button.exit:
        # Clear the screen
        screen.fill(BACKGROUND)
        
        # Run through events
        for event in pygame.event.get():
            # If close pressed then quit game
            if event.type == pygame.QUIT:
                sys.exit()
            # If screen is resized then move items to new positions
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.size[0] if event.size[0] > 400 else 400, event.size[1] if event.size[1] > 400 else 400), pygame.RESIZABLE)
                for item in static_items:
                    item.update_pos(screen)
                    
        # Update and draw the static items
        static_items.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed(), screen)
        static_items.draw(screen)
        
        # Draw mouse
        if pygame.mouse.get_focused(): screen.blit(mouse.image, pygame.mouse.get_pos())
        pygame.display.update()
        clock.tick(60)
        
        music.play_music()
    
    ##pygame.quit()
    if music.song in music.songs:
        music.stop_music()
        
def options():
    pass