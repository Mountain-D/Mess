import pygame, sys, os, random

TILE_WIDTH = 64
TILE_HEIGHT = 32
FPS = 200
CLOCK = pygame.time.Clock()

from pygame.locals import *
pygame.init()

# Remove commented shit later
# pygame.display.set_caption('Mess')
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
# What is this class for? It looks useless:
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_surface):
        super().__init__()
        self.tile_surface = tile_surface
        self.rect = self.tile_surface.get_rect()


tileset_img = pygame.image.load('junk/tilesetmelkas.png')
tile_water = Tile(pygame.Surface.subsurface(tileset_img, (19, 147, TILE_WIDTH, TILE_HEIGHT)))
tile_grass = Tile(pygame.Surface.subsurface(tileset_img, (147, 73, TILE_WIDTH, TILE_HEIGHT)))
tile_dirt = Tile(pygame.Surface.subsurface(tileset_img, (147, 147, TILE_WIDTH, TILE_HEIGHT)))

# I don't see how this helps - you have 3 groups and each of them contains just 1 object of the Tile ¯\_(ツ)_/¯
# water_group = pygame.sprite.Group()
# grass_group = pygame.sprite.Group()
# dirt_group = pygame.sprite.Group()
#
# water_group.add(tile_water)
# grass_group.add(tile_grass)
# dirt_group.add(tile_dirt)


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

    # Option #2:
    # This is an array of objects which we would check for collision later, like water, walls and trees
    # bad_rect_arrays = []
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            # You're already doing a lot of calculations each frame. Better to do not repeat yourself:
            x_tile_location = 160 + x * 32 - y * 32
            y_tile_location = 100 + x * 16 + y * 16
            current_position = pygame.Rect(x_tile_location, y_tile_location, TILE_WIDTH, TILE_HEIGHT)
            if tile == 1:
                screen.blit(tile_water.tile_surface, current_position)

                # Option #1 - currently running:
                if pygame.Rect.colliderect(player.rect, current_position):
                    print('oops')

                # If you want to use a Tile as an object here, this 'if' check (above) can be implemented as
                # a Tile's function (added under Tile class, with an extra logic if required),
                # but Tile in this case should not use Surface class in the constructor
                # (constructor is what you use when you create an instance of an object - see lines 40-42)
                # because it does not carry information about current position.
                # If you look at the Surface description it says:
                # "Surface((width, height)...)"
                # i.e. surface default values are just width and height of the surface + the picture

                # Option #2:
                # bad_rect_arrays.append(current_position)

            elif tile == 2:
                screen.blit(tile_grass.tile_surface, current_position)
            elif tile == 3:
                screen.blit(tile_dirt.tile_surface, current_position)

    # Option #2:
    # or 'slower' option (depends on how many blocking tiles do you have):
    # for bad_rect in bad_rect_arrays:
    #     if pygame.Rect.colliderect(player.rect, bad_rect):
    #         print('oops')
    # On my ancient laptop this app already runs at max of 115fps on land an around 90-100 on water
    # so it's important for me :)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # water_group.update()
    # grass_group.update()
    # dirt_group.update()
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    CLOCK.tick(FPS)
    # Let's check the performance - look at how FPS drops when you try to move the mouse of walk to the land
    pygame.display.set_caption('Mess' + ' ' * 10 + 'FPS: ' + str(int(CLOCK.get_fps())))