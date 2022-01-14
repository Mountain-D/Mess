import pygame, sys, os, random

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Mess')
logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)
WINDOW_SIZE = (1024, 800)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((900, 900))

                ###

#SPRITE STUFF

class Tile(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

tileset_img = pygame.image.load('junk/tilesetmelkas.png')
tile_water = Tile(pygame.Surface.subsurface(tileset_img, (19, 147, 64, 36)))
tile_grass = Tile(pygame.Surface.subsurface(tileset_img, (147, 73, 64, 36)))
tile_dirt = Tile(pygame.Surface.subsurface(tileset_img, (147, 147, 64, 36)))

tile_group = pygame.sprite.Group()

tile_group.add(tile_water)
tile_group.add(tile_grass)
tile_group.add(tile_dirt)

#player sprite not done
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
    def player_location(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def walking(self):
        self.is_walk = True

    def swim(self):
        self.is_swim = True

   def update(self):
       if self.is_swim == True:




walking = Player(pygame.image.load('junk/player_img.png'))
swiming = Player(pygame.image.load('junk/player_img_swim.png'))

player_group = pygame.sprite.Group()

player_group.add(walking)
player_group.add(swiming)

#MAP READ

f = open('junk/map.txt')
map_data = [[int(column) for column in row] for row in f.read().split('\n')]
f.close()

#???scroll and move NEED TO ORGANIZE THIS

moving_right = False
moving_left = False
moving_up = False
moving_down = False

true_scroll = [0, 0]

player_location = [400, 400]

'''
player_rect = pygame.Rect(player_location[0], player_location[1], player_img.get_width(), player_img.get_height())
'''

#GAME LOOP mess as well

while True:
    display.fill((0, 0, 0))

    true_scroll[0] += (Player.x - true_scroll[0] - 420) / 10
    true_scroll[1] += (Player.y - true_scroll[1] - 420) / 10
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    Player.x = player_location[0]
    Player.y = player_location[1]

    player_movement = [0, 0]

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4
    if moving_up == True:
        player_location[1] -= 4
    if moving_down == True:
        player_location[1] += 4

    tiles = []
    water_tile = []
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                display.blit(tile_1, ((160 + x * 32 - y * 32) - scroll[0], (100 + x * 16 + y * 16) - scroll[1]))
            if tile == 2:
                display.blit(tile_2, ((160 + x * 32 - y * 32) - scroll[0], (100 + x * 16 + y * 16) - scroll[1]))
            if tile == 3:
                display.blit(tile_3, ((160 + x * 32 - y * 32) - scroll[0], (100 + x * 16 + y * 16) - scroll[1]))



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