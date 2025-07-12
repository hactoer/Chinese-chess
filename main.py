import pygame
from ui.screen import *
from game.playgame import *
pygame.init()
def main():
    pygame.init()
    LoadING(skip=True)
    a=MainOption()
    InitGame()
    game(a)
    pygame.quit()
if __name__=='__main__':
    main()