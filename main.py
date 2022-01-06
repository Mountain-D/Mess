import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Mess')
logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((1024, 800))
display = pygame.Surface((800, 800))

tileset_img = pygame.image.load('junk/tilesetmelkas.png').convert()

f = open('junk/map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0, 0, 0))

    for y, row in enumerate(map_data):
        for x,tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (360 + x * 32 - y * 32, 200 + x * 16 + y * 16), (19, 147, 64, 36))
            if tile == 2:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (360 + x * 32 - y * 32, 200 + x * 16 + y * 16), (147, 73, 64, 36))
            if tile == 3:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (360 + x * 32 - y * 32, 176 + x * 16 + y * 16), (147, 13, 64, 60))
            if tile == 4:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(tileset_img, (360 + x * 32 - y * 32, 200 + x * 16 + y * 16), (147, 147, 64, 36))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()