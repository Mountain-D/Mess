import random

import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Mess')
logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)
WINDOW_SIZE = (1024, 800)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((900, 900))

tileset_img = pygame.image.load('junk/tilesetmelkas.png').convert()

tile_1 = tileset_img.subsurface((19, 147, 64, 36))
tile_2 = tileset_img.subsurface((147, 73, 64, 36))
tile_3 = tileset_img.subsurface((147, 13, 64, 60))
tile_4 = tileset_img.subsurface((147, 147, 64, 36))

player_img = pygame.image.load('junk/player_img.png')

moving_right = False
moving_left = False
moving_up = False
moving_down = False

true_scroll = [0, 0]

player_location = [200, 400]

player_rect = pygame.Rect(player_location[0], player_location[1], player_img.get_width(), player_img.get_height())

f = open('junk/map.txt')
map_data = [[int(column) for column in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0, 0, 0))

    true_scroll[0] += (player_rect.x-true_scroll[0]-420)/10
    true_scroll[1] += (player_rect.y-true_scroll[1]-420)/10
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    if moving_up == True:
        player_location[1] -= 4
    if moving_down == True:
        player_location[1] += 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                display.blit(tile_1, ((160 + x * 32 - y * 32)- scroll[0], (100 + x * 16 + y * 16)- scroll[1]))
            if tile == 2:
                display.blit(tile_2, ((160 + x * 32 - y * 32)- scroll[0], (100 + x * 16 + y * 16)- scroll[1]))
            if tile == 3:
                display.blit(tile_3, ((160 + x * 32 - y * 32)- scroll[0], (76 + x * 16 + y * 16)- scroll[1]))
            if tile == 4:
                display.blit(tile_4, ((160 + x * 32 - y * 32)- scroll[0], (100 + x * 16 + y * 16)- scroll[1]))

    display.blit(player_img, (player_rect.x- scroll[0], player_rect.y- scroll[1]))

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
            if event.key == K_w:
                moving_up = True
            if event.key == K_s:
                moving_down = True
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False
            if event.key == K_w:
                moving_up = False
            if event.key == K_s:
                moving_down = False


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(60)