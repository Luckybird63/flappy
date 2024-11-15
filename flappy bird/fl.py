import random # for generating random numbers
import sys # we will use sys.exit to exit the program
import pygame
import pygame.locals import * # basic pygame imports

#global variables for the game 
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN  = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = '/gallery/sprites/bird.png'
BACKGROUND = '/gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
if_name == "_main_":
# This will be our main point from where our game will start
pygame.init()# Initialize all pygame's module
FPSCLOCK = pygame.time.Clock()
pygame.display.pygame.display.set_caption(title, icontitle=None)
GAME_SPRITES['numbers']= (
    pygame.image.load('/gallery/sprites/0.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/1.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/2.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/3.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/4.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/5.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/6.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/7.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/8.png').pygame.Surface.convert_alpha(),
    pygame.image.load('/gallery/sprites/9.png').pygame.Surface.convert_alpha(),
)
GAME_SPRITES['message'] = pygame.image.load('/gallery/sprites/message.png').pygame.Surface.convert_alpha()
GAME_SPRITES['base'] = pygame.image.load('/gallery/sprites/message.png').pygame.Surface.convert_alpha()
GAME_SPRITES['pipe'] = ( pygame.transform.rotate(pygame.image.load((PIPE).pygame.Surface.convert_alpha() ,180),
    pygame.image.load(PIPE).pygame.Surface.convert_alpha()
)
# Game sounds
GAME_SOUNDS['die'] = pygame.image.load('/gallery/sprites/die.png')
GAME_SOUNDS['hit'] = pygame.image.load('/gallery/sprites/hit.png')
GAME_SOUNDS['point'] = pygame.image.load('/gallery/sprites/point.png')
GAME_SOUNDS['swoosh'] = pygame.image.load('/gallery/sprites/swoosh.png')
GAME_SOUNDS['wing']    = pygame.image.load('/gallery/sprites/wing.png')
GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player']    = pygame.image.load(PLAYER).convert_alpha()












