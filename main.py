import pygame
from asserts.images import images 
screen=pygame.display.set_mode((800,600))
a=True
while a:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            a=False
    screen.blit(images.chessboard,(0,0))    
    pygame.display.flip()

