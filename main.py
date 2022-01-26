    #IMPORT & WHATEVER

import pygame, sys, os, random, math, numpy

from pygame.locals import *
from player import Player

    #INITIATE

pygame.init()

    #DEFINE STUFF

def render(x, y, screen, player):

    player.render(x, y, screen)

def update(player):
    player.update()

    #VARIABLES

TILE_WIDTH = 64
TILE_HEIGHT = 32

true_scroll = [0, 0]

player = Player()

FPS = 60
WINDOW_SIZE = (800, 800)
DISPLAY_X = 800
DISPLAY_Y = 800

logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)

SCREEN = pygame.display.set_mode(WINDOW_SIZE)

DISPLAY = pygame.Surface((DISPLAY_X, DISPLAY_Y))

CLOCK = pygame.time.Clock()

    #LOAD MEDIA & GET COLLIDE_MASKS

tileset_img = pygame.image.load('junk/tilesetmelkas.png').convert_alpha()
tile_water = pygame.Surface.subsurface(tileset_img, (19, 147, TILE_WIDTH, TILE_HEIGHT))
tile_grass = pygame.Surface.subsurface(tileset_img, (147, 73, TILE_WIDTH, TILE_HEIGHT))
tile_dirt = pygame.Surface.subsurface(tileset_img, (147, 147, TILE_WIDTH, TILE_HEIGHT))

tile_water_mask = pygame.mask.from_surface(tile_water)
tile_grass_mask = pygame.mask.from_surface(tile_grass)
tile_dirt_mask = pygame.mask.from_surface(tile_dirt)


    #READ MAP

with open('junk/maps_dump/map_test_gen.txt', 'r') as f:
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
    CLOCK.tick(FPS)
    pygame.display.set_caption('Mess' + ' ' * 10 + 'FPS: ' + str(int(CLOCK.get_fps())))

    #RENDER

    SCREEN.blit(pygame.transform.scale(DISPLAY, WINDOW_SIZE), (0, 0))

    SCREEN.fill((120, 120, 120))

    true_scroll[0] += (player.x-true_scroll[0] - 370) / 10
    true_scroll[1] += (player.y-true_scroll[1] - 370) / 10
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    cord_x = (scroll[0] + scroll[1] * 2) / 2
    cord_y = scroll[1] - scroll[0] / 2
    tile_x = round(cord_x / 32)
    tile_y = round(cord_y / 32)
    tile_coord = (tile_x, tile_y)

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):

            x_tile_location = 400 + x * 32 - y * 32 - scroll[0]
            y_tile_location = 400 + x * 16 + y * 16 - scroll[1]
            offset_x = x_tile_location - 370
            offset_y = y_tile_location - 370
            current_position = pygame.Rect(x_tile_location, y_tile_location, TILE_WIDTH, TILE_HEIGHT)


            if tile == 1:
                SCREEN.blit(tile_water, current_position)
                if player.mask.overlap(tile_water_mask, (offset_x, offset_y)):
                    player.swiming = True
                    player.walking = False

            elif tile == 2:
                SCREEN.blit(tile_grass, current_position)
                if player.mask.overlap(tile_grass_mask, (offset_x, offset_y)):
                    player.walking = True
                    player.swiming = False

            elif tile == 3:
                SCREEN.blit(tile_dirt, current_position)
                if player.mask.overlap(tile_dirt_mask, (offset_x, offset_y)):
                    player.walking = True
                    player.swiming = False



    render(0 - scroll[0], 0 - scroll[1], SCREEN, player)

    print(f' current tile : {tile_coord} \n ***********************************')