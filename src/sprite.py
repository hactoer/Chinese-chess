import pygame
from UnitChanger import *
from asserts.images.images import *
import numpy as np
from ui.screen import screen
Matrix=np.array([[0]*9 for i in range(10)])
class Center(pygame.sprite.Sprite):
    def __init__(self,position:tuple,image:pygame.Surface):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.position=position
        self.rect.center=position
    def init(self):
        Matrix=[
            ['rch','rho','rel','rad','rge','rad','rel','rho','rch'],
            ['000','000','000','000','000','000','000','000','000'],
            ['000','rca','000','000','000','000','000','rca','000'],
            ['rso','000','rso','000','rso','000','rso','000','rso'],
            ['000','000','000','000','000','000','000','000','000'],
            ['000','000','000','000','000','000','000','000','000'],
            ['bso','000','bso','000','bso','000','bso','000','bso'],
            ['000','bca','000','000','000','000','000','bca','000'],
            ['000','000','000','000','000','000','000','000','000'],
            ['bch','bho','bel','bad','bge','bad','bel','bho','bch']
        ]
        Dict={
                'rch':rchariots,
                'rho':rhorses,
                'rel':relephants,
                'rad':radvisors,
                'rge':rgeneral,
                'rca':rcannos,
                'rso':rsoiders,
                'bch':bchariots,
                'bho':bhorses,
                'bel':belephants,
                'bad':badvisors,
                'bge':bgeneral,
                'bca':bcannos,
                'bso':bsoiders,
            }
        for i,j in Matrix:
            if Matrix[i][j]!='000':
                screen
    def check(self,mospos):
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                
