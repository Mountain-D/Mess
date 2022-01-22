import pygame, sys, os, random, math, numpy
from pygame.locals import *

class Player:
    def __init__(self):
        #SPAWN COORD(SCREEN)
        self.x = 400
        self.y = 400

        self.velocity = 0
        self.acceleration = 1
        self.topSpeed = 8

        self.swim = pygame.image.load('junk/player_img_swim.png')
        self.walk = pygame.image.load('junk/player_img.png')
        self.rect = self.walk.get_rect()
        self.collide = pygame.image.load('junk/player_cillision_mask.png')
        self.mask = pygame.mask.from_surface(self.collide)
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.image = self.walk

        self.swiming = False
        self.walking = False

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

    def render(self, x, y, screen):
        self.rect.x += x
        self.rect.y += y
        screen.blit(self.image, self.rect)

        if self.swiming == True:
            self.image = self.swim

        if self.walking == True:
            self.image = self.walk

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