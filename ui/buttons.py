from asserts.images.images import *
import pygame
from tool.Constants import *
mode=None
class Button(pygame.sprite.Sprite):
    def __init__(self,image,position,mode):
        super().__init__()
        self.image=image
        self.position=position
        self.rect=self.image.get_rect()
        self.rect.center=position
        self.mode=mode
    def update(self,mousepos):
        global mode
        if self.rect.collidepoint(mousepos):
            self.image=pygame.transform.scale2x(self.image)
        else:
            self.image=pygame.transform.scale(self.image,ButtonSize)
    def kill(self):
        pygame.sprite.Sprite.kill(self)
    def Clicked(self):
        global mode
        self.mode=mode
class twoplayer(Button):
    def __init__(self):
        super().__init__(TwoPlayerButton,
                         (ScreenSize[0]//2-20,ScreenSize[1]//2-20),
                         'TwoPlayer')
    def update(self,mousepos):
        super().update(mousepos)
    def kill(self):
        super().kill()
class aiplayer(Button):
    def __init__(self):
        super().__init__(AIPlayerButton,
                         (ScreenSize[0]//2-20,ScreenSize[1]//2+150),
                         'AIPlayer')
    def update(self,mousepos):
        super().update(mousepos)
    def kill(self):
        super().kill()
    def Clicked(self):
        super().Clicked()
ButtonGroup=pygame.sprite.Group()
ButtonGroup.add(twoplayer(),aiplayer())
mode=None