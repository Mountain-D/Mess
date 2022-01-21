    #IMPORT & WHATEVER

import pygame, sys, os, random, opensimplex

from pygame.locals import *

    #INITIATE

pygame.init()

    #DEFINE STUFF


    #VARIABLES

FPS = 60
WINDOW_SIZE = (800, 800)
DISPLAY_X = 800
DISPLAY_Y = 800

logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)

SCREEN = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

DISPLAY = pygame.Surface((DISPLAY_X, DISPLAY_Y))

CLOCK = pygame.time.Clock()

blank_tile = [[1] * 200] * 200

    #MAP READ / WRITE

with open('junk/maps_dump/map_test_gen.txt', 'r') as f:
    map_data = [[int(column) for column in row] for row in f.read().split('\n')]

    #CREATE 200 * 200 BLANK [1] TILEMAP

with open('junk/maps_dump/map_test_gen.txt', 'w') as f:
    for line in blank_tile:
        line_str = [str(n) for n in line]
        f.write(''.join(line_str) + '\n')

        #GAME LOOP

while True:

    #EVENT

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #UPDATE

    pygame.display.update()
    CLOCK.tick(FPS)
    pygame.display.set_caption('Mess' + ' ' * 10 + 'FPS: ' + str(int(CLOCK.get_fps())))

    #RENDER



    SCREEN.blit(pygame.transform.scale(DISPLAY, WINDOW_SIZE), (0, 0))

    SCREEN.fill((120, 120, 120))

