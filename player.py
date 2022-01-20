import pygame, sys, os, random
from pygame.locals import *
from math import *

class Player:
    def __init__(self):
        self.x = 370
        self.y = 370

        self.velocity = 0
        self.acceleration = 1
        self.topSpeed = 8

        self.walk = pygame.image.load('junk/player_img.png')
        self.rect = self.walk.get_rect()
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def update(self):
        if self.left:
            self.x -= 3
        if self.right:
            self.x += 3
        if self.up:
            self.y -= 3
        if self.down:
            self.y += 3

        self.rect.x = self.x
        self.rect.y = self.y

    def render(self, x, y, sceen):
        sceen.blit(self.walk, self.rect)

    def key_down(self, key):
        if key == pygame.K_a:
            self.left = True
        if key == pygame.K_d:
            self.right = True
        if key == pygame.K_w:
            self.up = True
        if key == pygame.K_s:
            self.down = True

    def key_up(self, key):
        if key == pygame.K_a:
            self.left = False
        if key == pygame.K_d:
            self.right = False
        if key == pygame.K_w:
            self.up = False
        if key == pygame.K_s:
            self.down = False