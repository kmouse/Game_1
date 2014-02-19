import pygame
from player import Player
from effectors import Black_Hole

class Game:
    def __init__(self, screen, size, start, items):
        # Create the level boundaries
        self.image = pygame.Surface(size)
        
        # Create draw area, how much of the screen is shown
        x, y = screen.get_size()
        self.draw_area = pygame.Rect((0, 0), (x - 200, y))
        
        # Top-left of screen
        self.pos = [0, 0]
        
        # List of effectors
        effectors = []
        
        ## TEMP-REMOVE URGENT
        pygame.draw.circle(self.image, (255, 255, 255), self.pos, 10)
        
        # Monitor if the screen can be moved on mouse press
        self.allow_move = 1
        
        self.player = pygame.sprite.Group()
        Player.containers = self.player
        
        self.effectors = pygame.sprite.Group()
        Black_Hole.containers = self.effectors
        for item in items:
            item = item.split(":")
            print (item)
            if item[0] == "Player":
                x, y, angle, velocity = item[1].split(",")
                Player(int(x), int(y), float(angle), float(velocity))
            elif item[0] == "Black Hole":
                x, y, = item[1].split(",")
                Black_Hole(int(x), int(y))
        
    def update_size(self, screen):
        # Update the size of the draw area on screen resize
        x, y = screen.get_size()
        self.draw_area = pygame.Rect((0, 0), (x - 200, y))
        
    def move(self):
        # Clear the screen
        self.image.fill((0, 0, 0))
        self.player.update([])
        self.player.draw(self.image)
        self.effectors.draw(self.image)
        # Get the new mouse events
        mouse = pygame.mouse.get_pressed()
        move = pygame.mouse.get_rel()
        
        # Move the screen if the mouse is pressed and the mouse was pressed on the game area
        mouse_rect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))
        ## POSSIBLE DODGY HACK
        screen_area = pygame.Rect(self.draw_area)
        screen_area.topleft = (0, 0)
        if screen_area.colliderect(mouse_rect):
            if mouse[2] and self.allow_move != 0:
                self.allow_move = 2
                self.pos[0] -= move[0]
                self.pos[1] -= move[1]
            elif not mouse[2] and self.allow_move == 0:
                self.allow_move = 1
        elif mouse[2] and self.allow_move != 2:
            self.allow_move = 0
        elif mouse[2] and self.allow_move == 2:
            self.pos[0] -= move[0]
            self.pos[1] -= move[1]
        else:
            self.allow_move = 0
            
        self.draw_area.topleft = self.pos
        
        game_draw_area = self.image.get_rect()
        game_draw_area.topleft = -self.draw_area.left, -self.draw_area.top
        if game_draw_area.width < screen_area.width and game_draw_area.height < screen_area.height:
            game_draw_area.clamp_ip(screen_area)
        
        self.draw_area.topleft = -game_draw_area.left, -game_draw_area.top