from Data.Code.side_menu import side_menu
from Data.Code.mouse import Mouse
from Data.Code.current_game import Game
from Data.Code.load import get_level, get_file, get_music, get_font
from Data.Code.level_select import Level_Select
from Data.Code.music_controls import Music_Controls
from Data.Code.cutscene import Cutscene
from Data.Code.credits import credits
from math import ceil
import pygame
import sys
import random
import ctypes

user32 = ctypes.windll.user32
SCREEN_SIZE = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        
START_SIZE = (700, 500)
MAX_SIZE = (700, 500)
        
def control_game():
    pygame.init()
    
    # If there is already a surface then use that
    # This is used to prevent an error with the surface mismatching to the screen
    old_screen = pygame.display.get_surface()
    if old_screen:
        old_size = old_screen.get_size()
        screen = pygame.display.set_mode((max(old_size[0], MAX_SIZE[0]), max(old_size[1], MAX_SIZE[1])), old_screen.get_flags())
        
    # Create the screen
    else:
        screen = pygame.display.set_mode(START_SIZE, pygame.RESIZABLE)
    pygame.mouse.set_visible(0)
    
    # Get the users requested level
    end_game = False
    end_select = False
    while not end_game and not end_select:
        level, end_select = level_select(screen)
        if not end_select:
            # Run the game
            end_game = run_game(screen, level)
    
    
def level_select(screen):

    BACKGROUND_COLOR = (15, 24, 122)
    
    TOP_SPACE = 200
    DIST = 140
    
    
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
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0, True
            if event.type == pygame.VIDEORESIZE:
                # maintain the flags of the surface
                old_screen = pygame.display.get_surface()
                screen = pygame.display.set_mode((max(event.size[0], MAX_SIZE[0]), max(event.size[1], MAX_SIZE[1])), old_screen.get_flags())
                with open(get_file("Levels/levels_info.txt")) as f:
                    num_levels = int(f.readline())
                    unlocked_levels = int(f.readline())
                selector = Level_Select(screen, num_levels, unlocked_levels)
            ## MAKE WORK NOT URGENT BUT SHOULD BE DONE BEFORE UPLOADING
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F11:
                    # get the flags of the surface
                    old_screen = pygame.display.get_surface()
                    
                    screen = pygame.display.set_mode((MAX_SIZE[0], MAX_SIZE[1]) if old_screen.get_flags() == pygame.FULLSCREEN else SCREEN_SIZE, 
                    pygame.RESIZABLE if old_screen.get_flags() == pygame.FULLSCREEN else pygame.FULLSCREEN)
                
        pressed = selector.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        screen.fill(BACKGROUND_COLOR)
        screen.blit(selector.image, (0, (TOP_SPACE - DIST / 2)))
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse.image, (x - 5, y - 5))
        pygame.display.update()
        
        
        if pressed or exit_game:
            break
    return pressed, exit_game
    
    
def run_game(screen, level):

    level_file = get_level(str(level) + ".txt")
    
    with open(level_file) as l:
        level_objects = l.read()
                
    # Get level items
    level_items, player_items, game_items = level_objects.split("--\n")
    level_items = level_items.split("\n")
    
    # Create the side menu and game
    menu_group = pygame.sprite.Group()
    side_menu.containers = menu_group
    
    # Initialise the side menu
    side = side_menu(screen, player_items.split("\n"))
    
    text = [" "]
    # How long each text lasts for
    text_time = 300
    text_timer = 0
    
    # Initialise game
    for item in level_items:
        item = item.split(":")
        if item[0] == "Screen":
            game_size = item[1].split(",")
        if item[0] == "Text":
            text.append(item[1])
        if item[0] == "Cutscene":
            cut = Cutscene(screen, item[1])
            show_cutscene = True
            while show_cutscene:
                screen.fill((0, 0, 0))
                screen.blit(cut.image, (screen.get_width() / 2 - cut.image.get_width() / 2, screen.get_height() / 2 - cut.image.get_height() / 2))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        show_cutscene = False
                    # If the window is resized then update all objects
                    if event.type == pygame.VIDEORESIZE:
                        old_screen = pygame.display.get_surface()
                        screen = pygame.display.set_mode((max(event.size[0], 700), max(event.size[1], 500)), old_screen.get_flags())
                        side.update_pos(screen)
                        play_area.update_size(screen)
        if item[0] == "Credits":
            credits(screen)
            font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
            text_render = font.render(" ", 1, (255, 255,255))
            with open(get_file("Levels/levels_info.txt")) as f:
                num_levels = f.readline()
                unlocked_levels = int(f.readline())
                
            with open(get_file("Levels/levels_info.txt"), "w") as f:
                max_level = max(unlocked_levels, level + 1)
                f.write(num_levels + str(max_level))
            return False
    
    play_area = Game(screen, (int(game_size[0]), int(game_size[1])), game_items.split("\n"))
    
    # Create music and additional music data
    music_group = pygame.sprite.Group()
    Music_Controls.containers = music_group
    music = Music_Controls(str(ceil((level * 8)/17)))
    music.play_music(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    side.commands.append("play game")
                    side.play()
            # If the window is resized then update all objects
            if event.type == pygame.VIDEORESIZE:
                old_screen = pygame.display.get_surface()
                screen = pygame.display.set_mode((max(event.size[0], 700), max(event.size[1], 500)), old_screen.get_flags())
                side.update_pos(screen)
                play_area.update_size(screen)
                font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
                text_render = font.render(text[0], 1, (255, 255,255))
                offset = [text_render.get_width() / 2, text_render.get_height() / 2]
                text_position = ((screen.get_width() / 2 - offset[0], screen.get_height() / 2 - offset[1]))
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_F11:
                    # get the flags of the surface
                    old_screen = pygame.display.get_surface()
                    
                    screen = pygame.display.set_mode((MAX_SIZE[0], MAX_SIZE[1]) if old_screen.get_flags() == pygame.FULLSCREEN else SCREEN_SIZE, 
                    pygame.RESIZABLE if old_screen.get_flags() == pygame.FULLSCREEN else pygame.FULLSCREEN)
                    
                    font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
                    text_render = font.render(text[0], 1, (255, 255,255))
                    offset = [text_render.get_width() / 2, text_render.get_height() / 2]
                    text_position = ((screen.get_width() / 2 - offset[0], screen.get_height() / 2 - offset[1]))
                
                
        # Update the side menu
        side.update(screen, play_area.pieces)
        play_area.pieces = []
        if "menu" in side.commands:
            font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
            text_render = font.render(" ", 1, (255, 255,255))
            return True
        if "level select" in side.commands:
            font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
            text_render = font.render(" ", 1, (255, 255,255))
            return False
        if "restart game" in side.commands:
            level_file = get_level(str(level) + ".txt")
    
            with open(level_file) as l:
                level_objects = l.read()
                        
            # Get level items
            level_items, player_items, game_items = level_objects.split("--\n")
            level_items = level_items.split("\n")
            #screen = pygame.display.set_mode(screen.get_size(), pygame.RESIZABLE)
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
            
            play_area = Game(screen, (int(game_size[0]), int(game_size[1])), game_items.split("\n"))
            
        
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
        
        # Draw the music controls
        music_group.draw(screen)
        
        # Draw text
        if text_timer == 0:
            text.pop(0)
            if len(text) == 0:
                text.append(" ")
            font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
            text_render = font.render(text[0], 1, (255, 255,255))
            offset = [text_render.get_width() / 2, text_render.get_height() / 2]
            text_position = ((screen.get_width() / 2 - offset[0], screen.get_height() / 2 - offset[1]))
            text_timer = text_time
                
        screen.blit(text_render, text_position)
        text_timer -= 1
        
        # Draw mouse
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            screen.blit(mouse.image, (x - 5, y - 5))
            
        # Draw screen
        pygame.display.update()
        
        # Cap framerate
        clock.tick(60)
        
        
        music.play_music(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            
        if play_area.finish == True:
            if play_area.loose == False:
                with open(get_file("Levels/levels_info.txt")) as f:
                    num_levels = f.readline()
                    unlocked_levels = int(f.readline())
                    
                with open(get_file("Levels/levels_info.txt"), "w") as f:
                    max_level = max(unlocked_levels, level + 1)
                    f.write(num_levels + str(max_level))
            
            font = pygame.font.Font(get_font('arial.ttf'), int(min((screen.get_width() / 700) * 20, 32)))
            text_render = font.render(" ", 1, (255, 255,255))
            return False