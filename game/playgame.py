#雙人對戰
import pygame
from src.sprite import screen,center
def two_player():
    run=True
    while run:
        mp=pygame.mouse.get_pos()
        center.check(mp)
