import pygame
from ui.screen import *
def main():
    pygame.init()
    LoadING(skip=True)
    MainOption()
    InitGame()
    pygame.quit()
if __name__=='__main__':
    main()