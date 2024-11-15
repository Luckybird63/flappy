import random
import sys
import pygame
import pygame.locals import *

#global variables
F = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN  = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = ''
BACKGROUND = ''
PIPE = ''
if_name == "_main_":
pygame.init()
FPSCLOCK = pygame.time.Clock()

