from side_menu import side_menu
from mouse import Mouse
from current_game import Game
from load import get_level, get_file, get_music
from level_select import Level_Select
from music import Music
from math import ceil
import pygame
import sys
import random
        
        
def control_game():
    pygame.init()
    # Create the screen
    screen = pygame.display.set_mode((700, 500), pygame.RESIZABLE)
    pygame.mouse.set_visible(0)
    print ("control game")
    # Get the users requested level
    end_game = False
    end_select = False
    while not end_game and not end_select:
        level, end_select = level_select(screen)
        if not end_select:
            # Run the game
            end_game = run_game(screen, level)
                
    ##pygame.quit()
    
    
def level_select(screen):
    print("level select")
    exit_game = False
    
    # Initialise the mouse
    mouse = Mouse()
    
    fullscreen = False
    
    with open(get_file("Levels/levels_info.txt")) as f:
        num_levels = int(f.readline())
        unlocked_levels = int(f.readline())
    selector = Level_Select(screen, num_levels, unlocked_levels)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.size[0] if event.size[0] > 700 else 700, event.size[1] if event.size[1] > 500 else 500), pygame.RESIZABLE)
                with open(get_file("Levels/levels_info.txt")) as f:
                    num_levels = int(f.readline())
                    unlocked_levels = int(f.readline())
                selector = Level_Select(screen, num_levels, unlocked_levels)
            ## MAKE WORK NOT URGENT BUT SHOULD BE DONE BEFORE UPLOADING
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F11:
                    fullscreen = not fullscreen
                    print("Fullscreeeen!!!")
                    pygame.display.set_mode((0,0), pygame.FULLSCREEN if fullscreen else pygame.RESIZABLE)
                
        pressed = selector.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        screen.blit(selector.image, (0, 0))
        if pygame.mouse.get_focused(): x, y = pygame.mouse.get_pos(); screen.blit(mouse.image, (x - 5, y - 5))
        pygame.display.update()
        
        
        if pressed or exit_game: break
    return pressed, exit_game
    
    
def run_game(screen, level):

    level_file = get_level(str(level) + ".txt")
    
    with open(level_file) as l:
        level_objects = l.read()
                
    # Get level items
    level_items, player_items, game_items = level_objects.split("--\n")
    level_items = level_items.split("\n")
    screen = pygame.display.set_mode(screen.get_size(), pygame.RESIZABLE)
    # Create the side menu and game
    menu_group = pygame.sprite.Group()
    side_menu.containers = menu_group
    
    # Initialise the side menu
    side = side_menu(screen, player_items.split("\n"))
    
    # Initialise game
    for item in level_items:
        item = item.split(":")
        if item[0] == "Screen":
            game_size = item[1].split(",")
    print(game_size, game_size)
    
    play_area = Game(screen, (int(game_size[0]), int(game_size[1])), game_items.split("\n"))
    
    # Create music and additional music data
    print(ceil((level * 8)/17))
    music = Music(str(ceil((level * 8)/17)))
    music.play_music()
    
    # Create the clock
    # This is used to limit the frame-rate
    clock = pygame.time.Clock()
    
    # Initialise the mouse
    mouse = Mouse()
    
    while True:
        for event in pygame.event.get():
            # If the close button is pressed then quit
            if event.type == pygame.QUIT:
                return True
            # If the window is resized then update all objects
            if event.type == pygame.VIDEORESIZE:
                print(event.size)
                screen = pygame.display.set_mode((event.size[0] if event.size[0] > 700 else 700, event.size[1] if event.size[1] > 500 else 500), pygame.RESIZABLE)
                side.update_pos(screen)
                play_area.update_size(screen)
                
                
        # Update the side menu
        side.update(screen)
        
        # Update the play area
        play_area.move(side.commands)
        
        # Remove the used commands
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
        
        
        music.play_music()
            
        if play_area.finish == True:
            if play_area.loose == False:
                with open(get_file("Levels/levels_info.txt")) as f:
                    num_levels = f.readline()
                    unlocked_levels = int(f.readline())
                    
                with open(get_file("Levels/levels_info.txt"), "w") as f:
                    max_level = max(unlocked_levels, level + 1)
                    f.write(num_levels + str(max_level))
                
            return False