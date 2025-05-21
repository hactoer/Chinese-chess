from asserts.images.images import *
import pygame
from tool.Constants import *
from src.sprite import screen
mode=None
class Button(pygame.sprite.Sprite):
    def __init__(self,image:pygame.Surface,position:tuple,mode):
        super().__init__()
        self.image=image
        self.Originalimage=image
        self.rect=self.image.get_rect()
        self.position=position
        self.rect.center=position
        self.mode=mode
        self.hover=False
    def update(self,mousepos):
        global mode
        is_hovered = (
            self.rect.left-20 < mousepos[0] < self.rect.right+20 and
            self.rect.top-20 < mousepos[1] < self.rect.bottom+20
        )
        if is_hovered and not self.hover:
            self.image=pygame.transform.scale2x(self.Originalimage)
            self.rect.center=(self.position[0]-50,self.position[1])
            self.hover=True
        elif self.hover and not is_hovered:
            self.image=self.Originalimage
            self.rect.center=self.position
            self.hover=False
class ButtonCentre:
    def __init__(self):
        self.image1=TwoPlayerButton
        self.image2=AIPlayerButton
        self.position1=(ScreenSize[0]//2-5,ScreenSize[1]//2-30)
        self.position2=(ScreenSize[0]//2-5,ScreenSize[1]//2+120)
        self.modeAI='AIPlayer'
        self.modeTP='TwoPlayer'
    def __enter__(self):
        self.tp=Button(
            self.image1,
            self.position1,
            self.modeTP
        )
        self.ai=Button(
            self.image2,
            self.position2,
            self.modeAI
        )
    def update(self,mousepos):
        self.tp.update(mousepos)
        self.ai.update(mousepos)
    def clicked(self,mousepos):
        if self.tp.rect.collidepoint(mousepos):
            global mode
            mode=self.tp.mode
            return True
        elif self.ai.rect.collidepoint(mousepos):
            global mode
            mode=self.ai.mode
            return True
        return None
    def __exit__(self,*_):
        return False
