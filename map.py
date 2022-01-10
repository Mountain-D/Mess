import random

import pygame, sys

from pygame.locals import *

f = open('junk/map.txt')
map_data = [[int(column) for column in row] for row in f.read().split('\n')]
f.close()

