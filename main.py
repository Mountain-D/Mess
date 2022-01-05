import pygame,sys

from pygame.locals import *

pygame.init()

pygame.display.set_caption('Mess')
logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((800,800))
display = pygame.Surface((300,300))

grass_img = pygame.image.load('junk/grass.png').convert()
grass_img.set_colorkey((0,0,0))
f = open('junk/map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0,0,0))

    for y,row in enumerate(map_data):
        for x,tile in enumerate(row):
            if tile:
                pygame.draw.rect(display,(255,255,255),pygame.Rect(x*10,y*10,10,10),1)
                display.blit(grass_img,(150+x*8-y*8,100+x*6+y*6))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))
    pygame.display.update()