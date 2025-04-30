import pygame
from asserts.images.images import * 
from INIT import version
from tool.Constants import *
from src.sprite import screen
from .buttons import *
import time
import random
def LoadING():
    pygame.display.set_caption(f'Chinese Chess {version}')
    screen.fill((BLACK))
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
def MainOption():
    global mode
    pygame.display.set_caption(f'Chinese Chess {version}')
    screen.fill(BACKGROUND)
    Run=True
    while Run:
        pygame.time.Clock().tick(60)
        mp=pygame.mouse.get_pos()
        print(mp,mode,sep=';')
        @Ckscreeninit
        def screeninit(mode):
            nonlocal mp
            mp=(0,0) if mp==None else mp
            global a
            pygame.display.set_caption(f'Chinese Chess {version}+::({mode})')
            screen.fill(BACKGROUND)
            screen.blit(chessboard,(BoundaryLength,0))
            a=True
        ButtonGroup.update(mp)
        ButtonGroup.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                screeninit(mode)
                Run=False
            if events.type==pygame.QUIT:
                Run=False
    ButtonGroup.kill()
def InitGame():
    global a
    while a:
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