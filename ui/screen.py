import pygame
from asserts.images import images
from INIT import version
from src.Constants import *
screen=pygame.display.set_mode((OriginalBoardSize[0]*2+BoundaryLength*2,OriginalBoardSize[1]*2+BoundaryLength))
pygame.display.set_caption(f'Chinese Chess {version}')
def S():
    screen.fill((247, 195, 110))
    screen.blit(images.chessboard,(BoundaryLength,0))
    pygame.display.update()
    pygame.display.flip()
    