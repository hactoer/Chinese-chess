import pygame
from UnitChanger import *
from asserts.images.images import *
import numpy as np
from ui.screen import screen
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
            'rch':(rchariots,...),
            'rho':(rhorses,...),
            'rel':(relephants,...),
            'rad':(radvisors,...),
            'rge':(rgeneral,...),
            'rca':(rcannos,...),
            'rso':(rsoiders,...),
            'bch':(bchariots,...),
            'bho':(bhorses,...),
            'bel':(belephants,...),
            'bad':(badvisors,...),
            'bge':(bgeneral,...),
            'bca':(bcannos,...),
            'bso':(bsoiders,...),
    }
class Center(pygame.sprite.Sprite):
    def init(self):
        for i,j in Matrix:
            if Matrix[i][j]!='000':
                screen.blit(Dict[Matrix[i][j]][0],MTP(i,j))
    def check(self,mospos:tuple):
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                if Matrix[PTM(*PF(mospos))] != '000':
                    print(Matrix[PTM(*PF(mospos))],PTM(*PF(mospos)))
                    self.RealPosition=PF(mospos)
                    self.MatrixIndex=PTM(*PF(mospos))
    def prerun(self):
       ...
        
        
