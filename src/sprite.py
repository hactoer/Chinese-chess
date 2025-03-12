import pygame
class Center(pygame.sprite.Sprite):
    def __init__(self,initposition,side,kind,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=initposition
        self.side=side
        self.kind=kind
    def check(self,MousePostion):
        ...
    def prerun(self):
        ...
    def run(self):
        ...
    def kill(self):
        ...

import pygame
class Center(pygame.sprite.Sprite):
    def __init__(self,initposition,side,kind,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=initposition
        self.side=side
        self.kind=kind
    def check(self,MousePostion):
        ...
    def prerun(self):
        ...
    def run(self):
        ...
    def kill(self):
        ...
    