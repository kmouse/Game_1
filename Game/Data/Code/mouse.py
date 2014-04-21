import pygame

TRANSPARENT = (0, 0, 0, 0)
BLACK = (0, 0, 0)
SIZE = (10, 10)

class Mouse:
    def __init__(self, color=(47, 204, 222)):
        self.image = pygame.Surface(SIZE, pygame.SRCALPHA)
        self.image.fill(TRANSPARENT)
        # Draw a circle with a black outline
        pygame.draw.circle(self.image, BLACK, (5, 5), 5)
        pygame.draw.circle(self.image, color, (5, 5), 4)