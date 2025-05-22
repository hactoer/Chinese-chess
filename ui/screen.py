import pygame
from asserts.images.images import * 
from INIT import version
from tool.Constants import *
from src.sprite import screen,center
from .buttons import *
import time
import random
from typing import Literal
def LoadING(skip=False):
    if skip:return
    pygame.display.set_caption(f'Chinese Chess {version}')
    screen.fill(BLACK)
    pygame.font.init()
    my_font=pygame.font.SysFont('Arial', 40)
    text=my_font.render('ProgrammerPython00', True, (WHITE))
    text_rect=text.get_rect(center=(ScreenSize[0]//2,ScreenSize[1]//2))
    screen.blit(text,text_rect)
    pygame.display.flip()
    for i in range(100):
        pygame.draw.rect(
            screen,
            WHITE,
            (0.2,ScreenSize[1]//1.5+30,ScreenSize[0]*i/100,20)
            )
        time.sleep(random.randint(1,10)*0.01)
        pygame.time.Clock().tick(60)
        pygame.display.flip()
def MainOption(instantmode:Literal['TwoPlayer','AIPlayer']=None):
    global mode,a
    a=False
    Run=True
    if instantmode:
        a=True
        Run=False
        pygame.display.set_caption(f'Chinese Chess {version}<{instantmode} mode>')
        return
    while Run:
        with ButtonCentre() as bc:
            screen.fill(BACKGROUND)
            pygame.display.set_caption(f'Chinese Chess {version}') 
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        a=False
                        Run=False
                    case pygame.MOUSEBUTTONDOWN:
                        bc.clicked(mp) if mp else None

            mp=pygame.mouse.get_pos()
            print(mp)
            bc.update(mp)
            screen.blit(bc.tp.image,bc.tp.rect)
            screen.blit(bc.ai.image,bc.ai.rect)
            pygame.display.flip()
            pygame.display.update()
            if mode:
                a=True
                Run=False
                match mode:
                    case 'AIPlayer':
                        print('AI')
                    case 'TwoPlayer':
                        print('TP')
                pygame.display.set_caption(f'Chinese Chess {version}<{mode} mode>')
                    
def InitGame():
    global a
    while a:
        screen.fill(BACKGROUND)
        screen.blit(chessboard,(12,8))
        center.init()
        fps=60
        clock=pygame.time.Clock()
        clock.tick(fps)
        mospos=pygame.mouse.get_pos()
        print(mospos)                    
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                mospos=pygame.mouse.get_pos()
            if events.type==pygame.QUIT:
                a=False
        pygame.display.flip()
        pygame.display.update()
