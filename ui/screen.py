import pygame
from asserts.images import images
from INIT import version
from src.UnitChanger import BoundaryLength
screen=pygame.display.set_mode((185*2+BoundaryLength*2,205*2+BoundaryLength))
pygame.display.set_caption(f'Chinese Chess {version}')
def S():
    screen.fill((247, 195, 110))
    screen.blit(images.chessboard,(BoundaryLength,0))
    pygame.display.update()
    pygame.display.flip()
    