import pygame
from Data.Code.load import get_level, get_font
from Data.Code.button import Button
from Data.Code.mouse import Mouse

PLAY_MUSIC = """import webbrowser
webbrowser.open(self.web)"""

def credits(screen):
    credits_location = get_level("credits.txt")
    with open(credits_location) as l:
        credit_modules = l.read()
        
    credit_modules = credit_modules.split("--")
    for module in credit_modules:
        items = module.split("\n")
        
        static_items = []
        static_item_pos = []
        
        buttons = pygame.sprite.Group()
        Button.containers = buttons
        
        for item in items:
            item = item.split(":")
            if item[0] == "Header":
                item[1] = item[1].split(",")
                font = pygame.font.Font(get_font('arial.ttf'), int(item[1][6]))
                static_items.append(font.render(item[1][0], 1, (int(item[1][1]), int(item[1][2]), int(item[1][3]))))
                if item[1][7] == "centre":
                    offset = [static_items[-1].get_width() / 2, static_items[-1].get_height() / 2]
                else:
                    offset = [0,0]
                static_item_pos.append((item[1][4] + "-" + str(offset[0]), item[1][5]  + "-" + str(offset[1])))
                    
            elif item[0] == "Button":
                item[1] = item[1].split(",")
                Button(screen, "", PLAY_MUSIC, item[1][0], item[1][1], width=150, height=150, image=item[1][2], highlight_image=item[1][2], pressed_image=item[1][2], image_align="topleft", init_command="self.web=\"" + item[1][3].replace(";", ":") + "\"")
            
        
        # Initialise the mouse
        mouse = Mouse()
    
        finished = False
        while not finished:
            screen.fill((0, 0, 0))
            i = 0
            for item in static_items:
                x = eval(static_item_pos[i][0], {"width":screen.get_width()})
                y = eval(static_item_pos[i][1], {"height":screen.get_height()})
                screen.blit(item,(x,y))
                i+=1
                
            x, y = pygame.mouse.get_pos()
            
            buttons.update((x, y), pygame.mouse.get_pressed(), screen)
            buttons.draw(screen)
                
            screen.blit(mouse.image, (x - 5, y - 5))
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.KEYDOWN:
                    finished = True
                # If the window is resized then update all objects
                if event.type == pygame.VIDEORESIZE:
                    old_screen = pygame.display.get_surface()
                    screen = pygame.display.set_mode((max(event.size[0], 700), max(event.size[1], 500)), old_screen.get_flags())
                    side.update_pos(screen)
                    play_area.update_size(screen)