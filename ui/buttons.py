from asserts.images.images import *
import pygame
from tool.Constants import *
mode=None
class Button(pygame.sprite.Sprite):
    def __init__(self,image:pygame.surface,position:tuple,mode):
        pygame.sprite.Sprite().__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.position=position
        self.rect.center=position
        self.mode=mode
    def update(self,mousepos):
        global mode
        if mousepos[0] in range(self.rect.left-10,self.rect.right+10)\
        and mousepos[1] in range(self.rect.top+10,self.rect.bottom-10):
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
    def Clicked(self):
        super().Clicked()
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
tp=twoplayer()
ap=aiplayer()
ButtonGroup.add(tp,ap)
mode=None