import pygame
from asserts.images import images
from INIT import version 
image=pygame.transform.scale2x(images.chessboard)
screen=pygame.display.set_mode(image.get_size())
pygame.display.set_caption(f'Chinese Chess {version}')
def S():
    screen.blit(image,(0,0))
    pygame.display.flip()