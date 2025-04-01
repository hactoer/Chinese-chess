import pygame
import asserts.images.images 
from INIT import version
from tool.Constants import *
from src.sprite import screen
def screeninit():
    pygame.init()
    pygame.display.set_caption(f'Chinese Chess {version}')
    a=True
    screen.fill((247, 195, 110))
    screen.blit(asserts.images.images.chessboard,(BoundaryLength,0))
