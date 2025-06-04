import pygame
from ui.screen import *
from game.playgame import *
def main():
    pygame.init()
    LoadING(skip=True)
    MainOption()
    InitGame()
    two_player()
    pygame.quit()
if __name__=='__main__':
    main()