import pygame
from asserts.images import images
from ui.screen import screen,S
pygame.init()
a=True
while a:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
    S()
