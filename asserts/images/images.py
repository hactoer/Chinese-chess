from pygame.image import load
from os.path import join 
def j(file):
    return join('assets','images',file)
chessboard=load(j('Chinese-chess-board.png'))
bsoiders=load(j('001.png'))
bcannos=load(j('002.png'))
bhorses=load(j('003.png'))
bchariots=load(j('004.png'))
belephants=load(j('005.png'))
badvisors=load(j('006.png'))
bgeneral=load(j('007.png'))
rsoiders=load(j('008.png'))
rcannos=load(j('009.png'))
rhorses=load(j('010.png'))
rchariots=load(j('011.png'))
relephants=load(j('012.png'))
radvisors=load(j('013.png'))
rgeneral=load(j('014.png'))
