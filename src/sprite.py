import pygame
from UnitChanger import *
from asserts.images.images import *
class Center(pygame.sprite.Sprite):
    def __init__(self,position:tuple,image:pygame.Surface):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.position=position
        self.rect.center=position
    def check(self,mospos):
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                ...  
                
