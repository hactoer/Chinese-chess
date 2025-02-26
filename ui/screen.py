import pygame
from asserts.images import images
image=pygame.transform.scale2x(images.chessboard)
screen=pygame.display.set_mode(image.get_size())
def S():
    screen.blit(image,(0,0))
    pygame.display.flip()
