import pygame
from ui.screen import *
from tool.Constants import *
def main():
    LoadING()
    screeninit()
    a=True
    while a:
        fps=60
        clock=pygame.time.Clock()
        clock.tick(fps)
        mospos=pygame.mouse.get_pos()
        print(mospos)                    
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                mospos=pygame.mouse.get_pos()
            if events.type==pygame.QUIT:
                a=False
        pygame.display.flip()
        pygame.display.update()
    pygame.quit()
if __name__=='__main__':
    main()