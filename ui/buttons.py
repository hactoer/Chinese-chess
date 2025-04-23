from asserts.images.images import *
import pygame
from tool.Constants import *
mode=None
class Button(pygame.sprite.Sprite):
    def __init__(self,image:pygame.surface,position:tuple,mode):
        pygame.sprite.Sprite().__init__(self)
        self.image=image
        self.Originalimage=image
        self.rect=self.image.get_rect()
        self.position=position
        self.rect.center=position
        self.mode=mode
        self.hover=False
    def kill(self):
        pygame.sprite.Sprite.kill(self)
    def update(self,mousepos):
        global mode
        is_hovered = (
            self.rect.left - 10 <= mousepos[0] <= self.rect.right + 10 |
            self.rect.top + 10 <= mousepos[1] <= self.rect.bottom - 10
        )
        if not self.hover & is_hovered:
            self.image=pygame.transform.scale2x(self.image)
            self.rect.center=self.position
        elif not is_hovered & self.hover:
            self.image=self.Originalimage
            self.rect.center=self.position
    def Clicked(self,mp):
        if self.rect.collidepoint(*mp):
            global mode
            self.mode=mode
class TP(Button):
    def __init__(self):
        super().__init__(TwoPlayerButton,
                         (ScreenSize[0]//2-40,ScreenSize[1]//2-30),
                         'TwoPlayer')
    def update(self,mousepos):
        super().update(mousepos)
    def kill(self):
        super().kill()
    def Clicked(self,mp):
        super().Clicked(mp)
class AI(Button):
    def __init__(self):
        super().__init__(AIPlayerButton,
                         (ScreenSize[0]//2-40,ScreenSize[1]//2+120),
                         'AIPlayer')
    def update(self,mousepos):
        super().update(mousepos)
    def kill(self):
        super().kill()
    def Clicked(self,mp):
        super().Clicked(mp)
tp=TP()
ai=AI()
ButtonGroup=pygame.sprite.Group()
ButtonGroup.add(tp)
ButtonGroup.add(ai)
def Ckscreeninit(f):
    def rapper(mp:tuple):
        global mode
        tp.Clicked(mp)
        ai.Clicked(mp)
        f(mode)
    return rapper
