import pygame, sys, os, random

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Mess')
logo = pygame.image.load("junk/Icon.png")
pygame.display.set_icon(logo)
WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display_x = 800
display_y = 800
display = pygame.Surface((display_x, display_y))


tileset_img = pygame.image.load('junk/tilesetmelkas.png')
tile_1 = pygame.Surface.subsurface(tileset_img, (19, 147, 64, 36))
tile_2 = pygame.Surface.subsurface(tileset_img, (147, 73, 64, 36))
tile_3 = pygame.Surface.subsurface(tileset_img, (147, 147, 64, 36))


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


water_group = pygame.sprite.Group()
grass_group = pygame.sprite.Group()
dirt_group = pygame.sprite.Group()

water_group.add(tile_water)
grass_group.add(tile_grass)
dirt_group.add(tile_dirt)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('junk/player_img.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = display_x / 2
        self.rect.bottom = display_y / 2
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = - 4
        if keys[pygame.K_d]:
            self.speedx = + 4
        if keys[pygame.K_w]:
            self.speedy = - 4
        if keys[pygame.K_s]:
            self.speedy = +4
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > display_x:
            self.rect.right = display_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > display_x:
            self.rect.bottom = display_y


player = Player()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)


                ###


#GAME LOOP mess as well

while True:

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    screen.fill((120, 120, 120))

    f = open('junk/map.txt')
    map_data = [[int(column) for column in row] for row in f.read().split('\n')]
    f.close()

    tiles = []
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:

                screen.blit(tile_1, ((160 + x * 32 - y * 32), (100 + x * 16 + y * 16)))
            if tile == 2:
                grass_group.draw(tile_2).copy()
                screen.blit(tile_2, ((160 + x * 32 - y * 32), (100 + x * 16 + y * 16)))
            if tile == 3:
                dirt_group.draw(tile_3)
                screen.blit(tile_3, ((160 + x * 32 - y * 32), (100 + x * 16 + y * 16)))

    if pygame.sprite.spritecollideany(player, water_group):
        print('opps')

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    water_group.update()
    grass_group.update()
    dirt_group.update()
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)