import pygame
from asserts.images.images import * 
from INIT import version
from tool.Constants import *
from src.sprite import screen
from .buttons import *
def LoadING():
    pygame.init()
    pygame.display.set_caption(f'Chinese Chess {version}')
    screen.fill((BLACK))
    pygame.font.init()
    my_font=pygame.font.SysFont('Arial', 40)
    text=my_font.render
    for i in range(100):
        pygame.draw.rect(
            screen,
            WHITE,
            (0,ScreenSize[1]//1.5+30,ScreenSize[0]*i%ScreenSize[0],10)
            )
        pygame.time.Clock().tick(60)
        pygame.display.flip()
def MainOption():
    pygame.init()
    pygame.display.set_caption(f'Chinese Chess {version}') 

def screeninit(mode):
    pygame.init()
    pygame.display.set_caption(f'Chinese Chess {version}'+'({mode})')
    a=True
    screen.fill((247, 195, 110))
    screen.blit(chessboard,(BoundaryLength,0))
