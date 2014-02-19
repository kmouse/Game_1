import pygame

class Mouse:
    def __init__(self, color=(47, 204, 222)):
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.circle(self.image, color, (5, 5), 5)