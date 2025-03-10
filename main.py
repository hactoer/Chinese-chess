import pygame
from ui.screen import S
from src.sprite import center
pygame.init()
fps=60
clock=pygame.time.Clock()
pygame.display.set_caption("棋盤圖片顯示")
a=True
center.init()
while a:
    clock.tick(fps)
    S()
    for events in pygame.event.get():
        if events.type==pygame.MOUSEBUTTONDOWN:
            mospos=pygame.mouse.get_pos()
        if events.type==pygame.QUIT:
            a=False
    S()
pygame.quit()
