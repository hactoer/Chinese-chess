import pygame
from ui.screen import S
from src.UnitChanger import BoundaryLength
from src.sprite import center
pygame.init()
fps=60
clock=pygame.time.Clock()
screen=pygame.display.set_mode((450+BoundaryLength*2,500+BoundaryLength))
pygame.display.set_caption("棋盤圖片顯示")
a=True
center.init()
while a:
    clock.tick(fps)
    screen.fill((247, 195, 110))
    S()
    for events in pygame.event.get():
        if events.type==pygame.MOUSEBUTTONDOWN:
            mospos=pygame.mouse.get_pos()
        if events.type==pygame.QUIT:
            a=False

pygame.quit()
