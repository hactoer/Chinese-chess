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
        self.is_hovered=None
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
            return True
        elif self.hover and not is_hovered:
            self.image=self.Originalimage
            self.rect.center=self.position
            self.hover=False
            return False
class ButtonCentre:
    def __init__(self):
        self.image1=TwoPlayerButton
        self.image2=AIPlayerButton
        self.position1=(ScreenSize[0]//2-5,ScreenSize[1]//2-30)
        self.position2=(ScreenSize[0]//2-5,ScreenSize[1]//2+120)
        self.modeAI='AIPlayer'
        self.modeTP='TwoPlayer'
        self.SelectedMode=None
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
        return self
    def update(self,mousepos):
        self.tp.update(mousepos)
        self.ai.update(mousepos)
        return
    def clicked(self,mp):
        if self.tp.hover:
            self.SelectedMode=self.modeTP
            print(f'Selected Mode: {self.SelectedMode}')
        elif self.ai.hover:
            self.SelectedMode=self.modeAI
            print(f'Selected Mode: {self.SelectedMode}')    
    def __exit__(self,*_):
        global mode
        print('Exiting ButtonCentre')
        if mode:
            return False