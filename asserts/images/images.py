from pygame.image import load
from os.path import join
from pygame.transform import scale,scale2x
import src.UnitChanger as UC
def joinpro(file):
    return join('asserts','images',file)
chessboard=scale2x(load(joinpro('Chinese-chess-board.png')))
rgeneral=scale(load(joinpro('001.png')),UC.r)
radvisors=scale(load(joinpro('002.png')),UC.r)
relephants=scale(load(joinpro('003.png')),UC.r)
rchariots=scale(load(joinpro('004.png')),UC.r)
rhorses=scale(load(joinpro('005.png')),UC.r)
rcannos=scale(load(joinpro('006.png')),UC.r)
rsoiders=scale(load(joinpro('007.png')),UC.r)
bgeneral=scale(load(joinpro('008.png')),UC.r)
badvisors=scale(load(joinpro('009.png')),UC.r)
belephants=scale(load(joinpro('010.png')),UC.r)
bchariots=scale(load(joinpro('011.png')),UC.r)
bhorses=scale(load(joinpro('012.png')),UC.r)
bcannos=scale(load(joinpro('013.png')),UC.r)
bsoiders=scale(load(joinpro('014.png')),UC.r)
preon=scale(load(joinpro('hint.png')),UC.r)

