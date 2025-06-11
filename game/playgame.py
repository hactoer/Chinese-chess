#雙人對戰
import pygame
from src.sprite import screen,center
def game(mode):
    run=True
    if mode=='TwoPlayer':
        while run:
            mp=pygame.mouse.get_pos()
            center.check(mp)
            center.run(mp)  # 拖曳棋子的畫面繪製
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    center.check(mp)
                if event.type==pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    center.dragging = False
                    center.drag_piece = None
    pygame.quit()