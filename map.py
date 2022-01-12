import random

import pygame, sys

from pygame.locals import *



f = open('junk/map.txt')
map_data = [[int(column) for column in row] for row in f.read().split('\n')]
f.close()

CHUNK_SIZE = 8

def generate_chunk(x, y):
    chunk_data = []
    tile_type = []
    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos
            target_y = y * CHUNK_SIZE + y_pos
            for y_pos, row in enumerate(map_data):
                for x_pos, tile in enumerate(row):
                    if map_data == 1:
                       tile_type = 1
                    elif map_data == 2:
                       tile_type = 2
                    elif map_data == 3:
                       tile_type = 3
                    if tile_type != 0:
                        chunk_data.append([[target_x, target_y], tile_type])
    return chunk_data
