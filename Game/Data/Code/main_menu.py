from button import Button
from image import Image
from mouse import Mouse
from music import Music
from load import get_image
import pygame
import sys
import ctypes
import logging

# Log debug and higher calls to this file
logging.basicConfig(filename='game.log', level=logging.DEBUG)

user32 = ctypes.windll.user32
SCREEN_SIZE = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

BACKGROUND = (239, 255, 168)
BLACK = (25, 25, 25)
WHITE = (225, 225, 225)
FPS = 60
START_SIZE = (640, 480)


def run_menu():
    logging.info("Initialising pygame")
    # Initialise pygame modules
    pygame.init()
    
    logging.info("Loading music")
    music = Music("Menu")
    music.play_music()
    
    logging.info("Creating new screen, overriding old")
    logging.info("Screen size: " + str(SCREEN_SIZE))
    logging.info("Screen flags: pygame.FULLSCREEN")
    # Create screen with size START_SIZE and allow resizing, give it an icon
    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
    pygame.display.set_icon(pygame.image.load(get_image("Static_Images\\icon.png")))
    
    # Hide the mouse
    pygame.mouse.set_visible(0)
    
    # Create a group to control and contain the button and image sprites
    static_items = pygame.sprite.Group()
    Button.containers = static_items
    Image.containers = static_items
    
    logging.info("Creating menu buttons")
    # Create the buttons
    start_button = Button(screen, "Start", "self.exit = True", "width/2", "((height - 220) / 8) * 1 + 220", init_command="self.exit = False")
    options_button = Button(screen, "Help", "print('1')", "width/2", "((height - 220) / 8) * 3 + 220")
    quit_button = Button(screen, "Quit", "import sys; sys.exit()", "width/2", "((height - 220) / 8) * 5 + 220")
    
    logging.info("Creating title")
    # Create the title
    Image(screen, "width/2", "120", image="Static_Images\\game_title.png")
    
    logging.info("Creating clock")
    # This is used to cap the framerate
    clock = pygame.time.Clock()
    
    logging.info("Creating mouse")
    mouse = Mouse()
    
    logging.info("Running menu event loop")
    # Run the menu
    while not start_button.exit:
        # Clear the screen
        screen.fill(BACKGROUND)
        
        # Run through events
        for event in pygame.event.get():
            # If close pressed then quit game
            if event.type == pygame.QUIT:
                logging.info("Close pressed, closing")
                sys.exit()
            # If screen is resized then move items to new positions
            if event.type == pygame.VIDEORESIZE:
                logging.debug("Screen resized, requested size: " + str(event.size[0]) + ", " + str(event.size[1]))
                # maintain the flags of the surface
                old_screen = pygame.display.get_surface()
                screen = pygame.display.set_mode((max(event.size[0], 400), max(event.size[1], 400)), old_screen.get_flags())
                logging.info("Moving item positions")
                for item in static_items:
                    item.update_pos(screen)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F11:
                    logging.debug("Fullscreen activated")
                    # get the flags of the surface
                    old_screen = pygame.display.get_surface()
                    
                    logging.info("Resizing screen")
                    screen = pygame.display.set_mode((START_SIZE[0], START_SIZE[1]) if old_screen.get_flags() == pygame.FULLSCREEN else SCREEN_SIZE, 
                    pygame.RESIZABLE if old_screen.get_flags() == pygame.FULLSCREEN else pygame.FULLSCREEN)
                    
   
        # Update and draw the static items
        static_items.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed(), screen)
        static_items.draw(screen)
        
        # Draw mouse
        if pygame.mouse.get_focused(): screen.blit(mouse.image, pygame.mouse.get_pos())
        
        # Draw frame
        pygame.display.update()
        
        # Cap fps
        clock.tick(FPS)
        
        # Play music
        music.play_music()
    
    # if the song playing is from the menu songs then stop the music
    if music.song in music.songs:
        music.stop_music()
        
def help():
    """Show the help page for the user"""
    pass