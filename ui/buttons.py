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
    def kill(self):
        pygame.sprite.Sprite.kill(self)
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
    def builder(self,screen:pygame.Surface):
        screen.blit(self.image,self.rect)
    def Clicked(self,mp):
        mp=(0,0) if mp is None else mp
        if self.rect.collidepoint(*mp):
            global mode
            mode=self.mode
    def kill(self):
        super().kill()
class TP(Button):
    def __init__(self):
        super().__init__(TwoPlayerButton,
                         (ScreenSize[0]//2-5,ScreenSize[1]//2-30),
                         'TwoPlayer')
class AI(Button):
    def __init__(self):
        super().__init__(AIPlayerButton,
                         (ScreenSize[0]//2-5,ScreenSize[1]//2+120),
                         'AIPlayer')
tp=TP()
ai=AI()
ButtonGroup=pygame.sprite.Group()
ButtonGroup.add(tp)
ButtonGroup.add(ai)
class BGfunction:
    def __init__(self):
        self.group=(tp,ai)
    def builder(self):
        for i in self.group:
            i.builder(screen)
    def kill(self):
        for i in self.group:
            i.kill()
    async def BC(self,mp):
        global a
        for i in self.group:
            i.Clicked(mp)
            for event in pygame.event.get():
                match event:
                    case pygame.MOUSEBUTTONDOWN:
                        pygame.display.set_caption(f'Chinese::{mode}')
                        a=True
                    case pygame.QUIT:
                        pygame.quit()
BGfunction=BGfunction()  


