import pygame
from ui.screen import S
from src.sprite import Center
Center=Center()
pygame.init()
a=True
while a:
    mospos=pygame.mouse.get_pos()
    print(mospos)
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            Center.init()
            
    S()
    
pygame.quit()