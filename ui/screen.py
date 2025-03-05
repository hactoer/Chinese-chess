import pygame
from asserts.images import images
from INIT import version
from src.UnitChanger import BoundaryLength
image=pygame.transform.scale2x(images.chessboard)
screen=pygame.display.set_mode((185+BoundaryLength*2,205+BoundaryLength))
pygame.display.set_caption(f'Chinese Chess {version}')
def S():
    screen.blit(image,(BoundaryLength,0))
    pygame.display.flip()