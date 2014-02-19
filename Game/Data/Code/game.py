from side_menu import side_menu
from mouse import Mouse
from current_game import Game
from load import get_level
import pygame
import sys

def control_game():
    pygame.init()
    # Create the screen
    screen = pygame.display.set_mode((700, 500), pygame.RESIZABLE)
    pygame.mouse.set_visible(0)
    print ("control game")
    # Get the users requested level
    level = level_select(screen)
    with open(level) as l:
        objects = l.read()
        # Run the game
        run_game(screen, objects)
    
    
def level_select(screen):
    print("level select")
    return get_level("1.txt")
    
    
def run_game(screen, level):
    # Get level items
    player_items, game_items = level.split("--\n")
    # Create the side menu and game
    menu_group = pygame.sprite.Group()
    side_menu.containers = menu_group
    
    # Initialise the side menu and game
    side = side_menu(screen, player_items.split("\n"))
    play_area = Game(screen, (700, 500), (440, 40), game_items.split("\n"))
    
    # Create the clock
    # This is used to limit the frame-rate
    clock = pygame.time.Clock()
    
    # Initialise the mouse
    mouse = Mouse()
    
    while True:
        for event in pygame.event.get():
            # If the close button is pressed then quit
            if event.type == pygame.QUIT:
                sys.exit()
            # If the window is resized then update all objects
            if event.type == pygame.VIDEORESIZE:
                print(event.size)
                screen = pygame.display.set_mode((event.size[0] if event.size[0] > 700 else 700, event.size[1] if event.size[1] > 500 else 500), pygame.RESIZABLE)
                side.update_pos(screen)
                play_area.update_size(screen)
                
        # Update the play area
        play_area.move()
        # Update the side menu
        side.update(screen)
        ## Urgent: make better codes
        for command in side.commands:
            if command == "Create Black Hole":
                print("Heya")
        side.commands = []
        # Draw the menu
        menu_group.draw(screen)
        screen_fill = pygame.Rect(play_area.draw_area)
        screen_fill.topleft = (0, 0)
        screen.fill((10, 20, 20), screen_fill)
        # Draw the game
        screen.blit(play_area.image, (0, 0), area=play_area.draw_area)
        # Draw mouse
        if pygame.mouse.get_focused(): x, y = pygame.mouse.get_pos(); screen.blit(mouse.image, (x - 5, y - 5))
        # Draw screen
        pygame.display.update()
        # Cap framerate
        clock.tick(60)