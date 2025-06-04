import pygame
from ui.screen import *
from game.playgame import *
def main():
    pygame.init()
    LoadING(skip=True)
    MainOption()
    two_player()
    InitGame()
    pygame.quit()
if __name__=='__main__':
    main()