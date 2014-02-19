from load import get_image
from calculations import get_distance, get_angle
import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, velocity):
        print(x, y, angle, velocity)
        # Initialise the sprite module
        pygame.sprite.Sprite.__init__(self, self.containers)
        # Make the image
        self.image = pygame.image.load(get_image("planet.png"))
        
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        
        self.mass = 20
        self.x, self.y = x, y
        self.velocity = velocity
        self.angle = angle
        self.lastangle = self.angle
        
        #work out the position of where this object would have been 1 frame ago
        self.lastpos = (self.x + (math.sin(self.angle + 3.14159265359)*self.velocity), self.y - (math.cos(self.angle + 3.14159265359)*self.velocity))

        self.killed = False;
        
    def update(self, effectors):
        #get the velocity and angle
        self.velocity = get_distance((self.x, self.y), self.lastpos)
        self.angle = get_angle(self.lastpos, (self.x, self.y))
            
        self.lastpos = (self.x, self.y)
        self.lastangle = self.angle
        #Move the object based on its new velocity and angle
        self.x += (math.sin(self.angle)*self.velocity)
        self.y -= (math.cos(self.angle)*self.velocity)

        #apply the gravity from each of the points
        for point in effectors:
            if point.type == "Black Hole":
                if get_distance((self.x, self.y), (point.x, point.y)) < point.mass:
                    self.kill()
                    self.killed = True
                    
                #get the needed values
                gravangle = get_angle((self.x, self.y), (point.x, point.y))
                #gravstrength = point.mass/(4*math.pi*get_distance((self.x, self.y), (point.x, point.y)))
                gravstrength = (1/(get_distance((self.x, self.y), (point.x, point.y))))*(point.mass)
                color = gravstrength * 500
                if color > 255:
                    color = 255
                #pygame.draw.line(screen, (255, 255, 255, color), (point.x, point.y), (self.x, self.y), 3)
                self.x += (math.sin(gravangle) * gravstrength)
                self.y -= (math.cos(gravangle) * gravstrength)
                color = int((255/1.0)*1*gravstrength)
                #just debugging info doesn't work with the new algorithim
                ##pygame.draw.line(screen, (color, color, 10), (self.x, self.y), (point.x, point.y), 1)
                        
            #apply the force from each of the  thrusters
            elif point.type == "Thruster":
                #get the needed values
                direction = thruster.angle
                strength = thruster.velocity
                #apply the force
                old = self.lastpos
                self.x += (math.sin(direction) * strength / self.mass)
                self.y -= (math.cos(direction) * strength / self.mass)
                
        self.rect.center = self.x, self.y