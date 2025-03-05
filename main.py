import pygame
from ui.screen import S
pygame.init()
a=True
while a:
    mospos=pygame.mouse.get_pos()
    print(mospos)
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
    S()
pygame.quit()