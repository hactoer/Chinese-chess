import pygame
from UnitChanger import *
class Center(pygame.sprite.Sprite):
    def __init__(self,initposition,side,kind,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=initposition
        self.side=side
        self.kind=kind
    def check(self,MousePostion:tuple):
        self.mpn=MousePostion[0]
        if self.rect.collidepoint(PF(*self.mp)):
            ...
    def prerun(self):
        ...
    def run(self):
        ...
    def kill(self):
        ...
    def bekill(self):
        ...