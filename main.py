import pygame
from ui.screen import S
from src.dfexception import NotSimplfiedException
pygame.init()
fps=60
clock=pygame.time.Clock()
screen=pygame.display.set_mode((185+BoundaryLength*2,205+BoundaryLength))
pygame.display.set_caption("棋盤圖片顯示")
a=True
while a:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    S()
    mospos=pygame.mouse.get_pos()
    print(mospos)
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            a=False

pygame.quit()
