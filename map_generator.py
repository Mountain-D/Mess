    #IMPORT & WHATEVER

import pygame, sys, os, random, math, numpy, opensimplex

from pygame.locals import *

    #INITIATE

pygame.init()

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

    #MAP READ / WRITE

#load_map_data = numpy.loadtxt('junk/maps_dump/map_test_gen.txt', delimiter=' ')

#CREATE 50 x 50 BLANK [1] TILEMAP

map_data = numpy.empty([50, 50])
map_data.fill(1)
save_map_data = numpy.savetxt('junk/maps_dump/map_test_gen.txt', map_data, fmt='%i', delimiter=' ')

        #GAME LOOP

while True:

    #EVENT

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #UPDATE

    event.type = QUIT

    pygame.display.update()
    CLOCK.tick(FPS)
    pygame.display.set_caption('Mess' + ' ' * 10 + 'FPS: ' + str(int(CLOCK.get_fps())))

    #RENDER



    SCREEN.blit(pygame.transform.scale(DISPLAY, WINDOW_SIZE), (0, 0))

    SCREEN.fill((120, 120, 120))

