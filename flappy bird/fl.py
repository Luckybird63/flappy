import random # for generating random numbers
import sys # we will use sys.exit to exit the program
import pygame
from import pygame .locals import *  # basic pygame imports

#global variables for the game 
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN  = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
def welcomeScreen():
    ...

    shows welcome images on the screen 
    ...
    playerx = int(SCREENWIDTH())
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()))/2
    messagey = int((SCREENHEIGHT *0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button close the game
            if event.type ==QUIT or (event.type== KEYDOWN and event.key==K_ESCAPE)
            Pygame.Quit()
            sys.exit()
            # if the user presses space or upkey start the game for them
            elif event.type == KEYDOWN or(event.key == SPACE or event.type == k_up):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def maingame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery= int(SCREENWIDTH/2)
    basex = 0
    # create two pipes for blinting on the screen
    newPipe1 = getRandomPipe()
    newPipe2=getRandompipe()

def getRandomPipe():
    ---
    generates position of two pipes(one bottom straight and one top rotated)for blitting the SCREEN
    ---
    pipeheight = GAME_SPRITES['pipe'][0].get_height();
    offset=SCREENHEIGHT/3;
    y2=offset+random.randrange(0,int(SCREENHEIGHT-GAME_SPRITES['base'].get_height()- 1.2*offset)) 
    pipex=SCREENWIDTH+10
    y1=pipeheight-y2+offset
    pipe =(
        ('x':pipex,'y':y1)#upper pipe
        ('x':pipex,'y':y2)#lower pipe
           ) 
        return pipe     
                    
                










    


if_name == "_main_":
# This will be our main point from where our game will start
pygame.init()# Initialize all pygame's module
FPSCLOCK = pygame.time.Clock()
pygame.display.pygame.display.set_caption(title, icontitle=None)
GAME_SPRITES['numbers']= (
    pygame.image.load('gallery/sprites/0.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/1.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/2.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/3.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/4.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/5.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/6.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/7.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/8.png').pygame.Surface.convert_alpha(),
    pygame.image.load('gallery/sprites/9.png').pygame.Surface.convert_alpha(),
)
GAME_SPRITES['message'] = pygame.image.load('gallery/sprites/message.png').pygame.Surface.convert_alpha()
GAME_SPRITES['base'] = pygame.image.load('gallery/sprites/base.png').pygame.Surface.convert_alpha()
GAME_SPRITES['pipe'] = ( pygame.transform.rotate(pygame.image.load((PIPE).pygame.Surface.convert_alpha() ,180),
    pygame.image.load(PIPE).pygame.Surface.convert_alpha()
)
# Game sounds
GAME_SOUNDS['die'] = pygame.image.load('gallery/sprites/die.png')
GAME_SOUNDS['hit'] = pygame.image.load('gallery/sprites/hit.png')
GAME_SOUNDS['point'] = pygame.image.load('gallery/sprites/point.png')
GAME_SOUNDS['swoosh'] = pygame.image.load('gallery/sprites/swoosh.png')
GAME_SOUNDS['wing']    = pygame.image.load('gallery/sprites/wing.png')
GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
GAME_SPRITES['player']    = pygame.image.load(PLAYER).convert_alpha()
while True:
    welcomeScreen() # shows welcome screen to the user until he press the button
    maingame() # This is the main game function












