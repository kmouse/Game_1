import pygame
from player import Player
from effectors import Black_Hole, Finish, Trigger_Left, Trigger_Right, Death

## # Music control buttons
## self.buttons.append(Button(self.image, "", "print('Back')", "40", "40", image="Buttons\\skip_backwards_button.png", highlight_image="Buttons\\skip_backwards_button_highlighted.png", pressed_image="Buttons\\skip_backwards_button_pressed.png", text_size=20))
        
## self.buttons.append(Button(self.image, "", "print('Play')", "width/2", "40", image="Buttons\\play_button.png", highlight_image="Buttons\\play_button_highlighted.png", pressed_image="Buttons\\play_button_pressed.png", text_size=20))
        
## self.buttons.append(Button(self.image, "", "print('Forward')", "width-40", "40", image="Buttons\\skip_forwards_button.png", highlight_image="Buttons\\skip_forwards_button_highlighted.png", pressed_image="Buttons\\skip_forwards_button_pressed.png", text_size=20))
        
        
class Game:
    def __init__(self, screen, size, items):
        # Create the level boundaries
        self.image = pygame.Surface(size)
        
        # Create draw area, how much of the screen is shown
        x, y = screen.get_size()
        self.draw_area = pygame.Rect((0, 0), (x - 200, y))
        
        # Top-left of screen
        self.pos = [int((size[0] - (screen.get_width() - 200)) / 2), int((size[1] - screen.get_height()) / 2)]
        
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
        Trigger_Left.containers = self.effectors
        Trigger_Right.containers = self.effectors
        Finish.containers = self.effectors
        Death.containers = self.effectors
        
        self.effectors_class = []
        for item in items:
            item = item.split(":")
            print (item)
            if item[0] == "Player":
                x, y, angle, velocity = item[1].split(",")
                Player(int(x), int(y), float(angle), float(velocity))
            elif item[0] == "Black Hole":
                x, y = item[1].split(",")
                self.effectors_class.append(Black_Hole(int(x), int(y)))
            elif item[0] == "Trigger_Left":
                x, y, width, height = item[1].split(",")
                self.effectors_class.append(Trigger_Left(int(x), int(y), int(width), int(height)))
            elif item[0] == "Trigger_Right":
                x, y, width, height = item[1].split(",")
                self.effectors_class.append(Trigger_Right(int(x), int(y), int(width), int(height)))
            elif item[0] == "Finish":
                x, y, width, height = item[1].split(",")
                self.effectors_class.append(Finish(int(x), int(y), int(width), int(height)))
            elif item[0] == "Death":
                x, y, width, height = item[1].split(",")
                self.effectors_class.append(Death(int(x), int(y), int(width), int(height)))
                
                
        self.simulate_game = False
        self.loose = False
                
        
    def update_size(self, screen):
        # Update the size of the draw area on screen resize
        x, y = screen.get_size()
        self.draw_area = pygame.Rect((0, 0), (x - 200, y))
        
    def move(self, commands):
        # Clear the screen
        self.image.fill((0, 0, 0))
        
        for command in commands:
            print(command)
            if command == "play game":
                self.simulate_game = True
            elif command == "Create Black Hole":
                self.effectors_class.append(Black_Hole(self.draw_area.width / 2, self.draw_area.height / 2))
            elif command == "Create Trigger Left":
                self.effectors_class.append(Trigger_Left(self.draw_area.width / 2, self.draw_area.height / 2, 150, 150))
            elif command == "Create Trigger Right":
                self.effectors_class.append(Trigger_Right(self.draw_area.width / 2, self.draw_area.height / 2, 150, 150))
                
        # Simulate game if true
        if self.simulate_game:
            self.player.update(self.effectors_class)
        else:
            for item in self.player:
                pygame.draw.line(self.image, (255, 0, 0), item.rect.center, (item.rect.centerx + (item.rect.centerx - item.lastpos[0]) * 25, item.rect.centery + (item.rect.centery - item.lastpos[1]) * 25), 1)
        self.finish = True
        for item in self.player:
            if item.finish == False:
                self.finish = False
            if item.killed == True:
                print("deaded")
                self.loose = True
                self.finish = True
        self.player.draw(self.image)
        self.effectors.draw(self.image)
        # Get the new mouse events
        mouse = pygame.mouse.get_pressed()
        move = pygame.mouse.get_rel()
        
        for item in self.effectors_class:
            item.update(pygame.mouse.get_pos(), mouse, self.pos)
        
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
        
        
        # Lock the game within the screen
        game_draw_area = self.image.get_rect()
        game_draw_area.topleft = -self.draw_area.left, -self.draw_area.top
            
        # Lock the game within the screen for the x axis
        if screen_area.width < game_draw_area.width:
            if game_draw_area.left > 0:
                game_draw_area.left = 0
                self.pos[0] = 0
            if game_draw_area.right < screen_area.width:
                game_draw_area.right = screen_area.width
                self.pos[0] = game_draw_area.width - screen_area.width
        else:
            extra_apace = screen_area.width - game_draw_area.width
            game_draw_area.left = extra_apace / 2
            self.pos[0] = -extra_apace / 2
            
        # Lock the game within the screen for the y axis
        if screen_area.height < game_draw_area.height:
            if game_draw_area.top > 0:
                game_draw_area.top = 0
                self.pos[1] = 0
            if game_draw_area.bottom < screen_area.height:
                game_draw_area.bottom = screen_area.height
                self.pos[1] = game_draw_area.height - screen_area.height
        else:
            extra_apace = screen_area.height - game_draw_area.height
            game_draw_area.top = extra_apace / 2
            self.pos[1] = -extra_apace / 2
        
        self.draw_area.topleft = -game_draw_area.left, -game_draw_area.top