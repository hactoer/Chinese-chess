import pygame
from UnitChanger import *
from asserts.images.images import *
class Center(pygame.sprite.Sprite):
    def __init__(self,initposition,side,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=initposition
        self.side=side
    def check(self,MousePostion:tuple):
        ...
    def prerun(self):
        ...
    def run(self):
        ...
    def kill(self):
        ...
    def bekill(self):
        ...