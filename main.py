    #IMPORT & WHATEVER

import pygame, sys, os, random

from pygame.locals import *
from math import *
from player import Player

def render(x, y, screen, player):

    player.render(x, y, screen)

def update(player):
    player.update()

    #INIT

pygame.init()

    #BASIC VARIABLES

TILE_WIDTH = 64
TILE_HEIGHT = 32

true_scroll = [0, 0]

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

    #READ MAP

with open('junk/map.txt') as f:
    map_data = [[int(column) for column in row] for row in f.read().split('\n')]


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

    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))

    screen.fill((120, 120, 120))

    true_scroll[0] += (player.x-true_scroll[0] - 370) / 10
    true_scroll[1] += (player.y-true_scroll[1] - 370) / 10
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):

            x_tile_location = 160 + x * 32 - y * 32 - scroll[0]
            y_tile_location = 100 + x * 16 + y * 16 - scroll[1]
            offset_x = x_tile_location - 370
            offset_y = y_tile_location - 370
            current_position = pygame.Rect(x_tile_location, y_tile_location, TILE_WIDTH, TILE_HEIGHT)

            if tile == 1:
                screen.blit(tile_water, current_position)
                if player.mask.overlap(tile_water_mask, (offset_x, offset_y)):
                    print('ooooh')

            elif tile == 2:
                screen.blit(tile_grass, current_position)
                #if player.mask.overlap(tile_grass_mask, (offset_x, offset_y)):


            elif tile == 3:
                screen.blit(tile_dirt, current_position)
                #if player.mask.overlap(tile_dirt_mask, (offset_x, offset_y)):


    render(0 - scroll[0], 0 - scroll[1], screen, player)
