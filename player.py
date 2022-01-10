import random

import pygame, sys

from pygame.locals import *

player_img = pygame.image.load('junk/player_img.png')
player_img_swim = pygame.image.load('junk/player_img_swim.png')

class player(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image(player_img)
        self.rect = self.image.get_rect()
        self.rect.