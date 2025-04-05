import pygame
from ui.screen import *
from tool.Constants import *
def main():
    pygame.init()
    LoadING()
    MainOption()
    a=True
    InitGame()
    pygame.quit()
if __name__=='__main__':
    main()