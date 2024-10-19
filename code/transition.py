import pygame
from settings import *

class Transition:
    def __init__(self, reset, player):
        # setup
        if not pygame.display.get_init():
            raise RuntimeError('Pygame display is not initialized')
        self.display_surface = pygame.display.get_surface()
        self.reset = reset
        self.player = player

        # overlay image
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SRCALPHA)
        self.color = 255
        self.speed = -2  # Default speed, can be adjusted dynamically if needed

    def play(self):
        self.color = max(0, min(self.color + self.speed, 255))
        if self.color <= 0:
            self.speed *= -1
            self.color = 0
            self.reset()
        if self.color > 255:
            self.color = 255
            self.player.sleep = False
            self.speed = -2

        self.image.fill((self.color, self.color, self.color))
        self.display_surface.blit(self.image, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

