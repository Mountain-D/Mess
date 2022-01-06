import random

import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Mess')
logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((1024, 800))
display = pygame.Surface((900, 900))

tileset_img = pygame.image.load('junk/tilesetmelkas.png').convert()
player_img = pygame.image.load('junk/player_img.png')

moving_right = False
moving_left = False
moving_up = False
moving_down = False

player_location = [200, 400]

f = open('junk/map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0, 0, 0))

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    if moving_up == True:
        player_location[1] -= 4
    if moving_down == True:
        player_location[1] += 4

    for y, row in enumerate(map_data):
        for x,tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (160 + x * 32 - y * 32, 100 + x * 16 + y * 16), (19, 147, 64, 36))
            if tile == 2:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (160 + x * 32 - y * 32, 100 + x * 16 + y * 16), (147, 73, 64, 36))
            if tile == 3:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (160 + x * 32 - y * 32, 76 + x * 16 + y * 16), (147, 13, 64, 60))
            if tile == 4:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (160 + x * 32 - y * 32, 100 + x * 16 + y * 16), (147, 147, 64, 36))

    display.blit(player_img, player_location)

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