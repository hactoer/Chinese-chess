import pygame
from ui.screen import S
from src.sprite import center
from asserts.images import images
from src.Constants import *
pygame.init()
fps=60
clock=pygame.time.Clock()
pygame.display.set_caption("棋盤圖片顯示")
a=True
center.init()
screen=pygame.display.set_mode((OriginalBoardSize[0]*2+BoundaryLength*2,OriginalBoardSize[1]*2+BoundaryLength))
screen.fill((247, 195, 110))
screen.blit(images.chessboard,(BoundaryLength,0))
while a:
    clock.tick(fps)
    mospos=pygame.mouse.get_pos()
    print(mospos)                     #之後必須得刪
    for events in pygame.event.get():
        if events.type==pygame.MOUSEBUTTONDOWN:
            mospos=pygame.mouse.get_pos()
        if events.type==pygame.QUIT:
            a=False
    S()
pygame.quit()
