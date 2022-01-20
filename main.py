    #IMPORT & WHATEVER

import pygame, sys, os, random

from pygame.locals import *
from math import *
from player import Player

def render(display, player):
    pygame.draw.rect(display, (255, 255, 255), (0 + player.x, 0 + player.y, 370, 370))
    player.render(player.x, player.y, screen)

def update(player):
    player.update()

    #INIT

pygame.init()

    #BASIC VARIABLES

TILE_WIDTH = 64
TILE_HEIGHT = 32

player = Player()

FPS = 200
WINDOW_SIZE = (800, 800)
display_x = 800
display_y = 800

logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

display = pygame.Surface((display_x, display_y))

CLOCK = pygame.time.Clock()

    #LOAD MEDIA & STUFF

tileset_img = pygame.image.load('junk/tilesetmelkas.png').convert_alpha()
tile_water = pygame.Surface.subsurface(tileset_img, (19, 147, TILE_WIDTH, TILE_HEIGHT))
tile_grass = pygame.Surface.subsurface(tileset_img, (147, 73, TILE_WIDTH, TILE_HEIGHT))
tile_dirt = pygame.Surface.subsurface(tileset_img, (147, 147, TILE_WIDTH, TILE_HEIGHT))

tile_water_mask = pygame.mask.from_surface(tile_water)
tile_grass_mask = pygame.mask.from_surface(tile_grass)
tile_dirt_mask = pygame.mask.from_surface(tile_dirt)

swim_img = pygame.image.load('junk/player_img_swim.png')
walk_image = pygame.image.load('junk/player_img.png')

player_col_mask = pygame.image.load('junk/player_cillision_mask.png')

player_mask = pygame.mask.from_surface(player_col_mask)

    #READ MAP

f = open('junk/map.txt')
map_data = [[int(column) for column in row] for row in f.read().split('\n')]
f.close()

        #GAME LOOP

while True:

    #EVENT

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYUP:
            player.key_up(event.key)
        if event.type == KEYDOWN:
            player.key_down(event.key)

    #UPDATE

    update(player)

    pygame.display.update()
    CLOCK.tick(60)
    pygame.display.set_caption('Mess' + ' ' * 10 + 'FPS: ' + str(int(CLOCK.get_fps())))

    #RENDER

    screen.fill((120, 120, 120))

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):

            x_tile_location = 160 + x * 32 - y * 32
            y_tile_location = 100 + x * 16 + y * 16
            offset_x = x_tile_location
            offset_y = y_tile_location
            current_position = pygame.Rect(x_tile_location, y_tile_location, TILE_WIDTH , TILE_HEIGHT)

            if tile == 1:
                screen.blit(tile_water, current_position)
                #if player_mask.overlap(tile_water_mask, (offset_x, offset_y)):
                  #  player_image = swim_img

            elif tile == 2:
                screen.blit(tile_grass, current_position)
                #if player.mask.overlap(tile_grass_mask, (offset_x, offset_y)):
                #    player.mage = walk_image

            elif tile == 3:
                screen.blit(tile_dirt, current_position)
                #if player.mask.overlap(tile_dirt_mask, (offset_x, offset_y)):
                #    player.image = walk_image

    render(display, player)