from src.sprite import Matrix,Dict
from src.UnitChanger import *
from ui.screen import screen
class Runner:
    def rch(self):
        i,j=PTM(*PF(self.position))
        x,y=PF(self.position)
        while Matrix[i][j]!='000':
            i+=1
            screen.bilt(Dict[Matrix[i][j]],(x,y))
        if 'b'==Matrix[i+1][j][0]:
            screen.bilt(Dict[Matrix[i+1][j]],(x,y))

    # Dict={
    #         'rch':(rchariots,...),
    #         'rho':rhorses,
    #         'rel':relephants,
    #         'rad':radvisors,
    #         'rge':rgeneral,
    #         'rca':rcannos,
    #         'rso':rsoiders,
    #         'bch':bchariots,
    #         'bho':bhorses,
    #         'bel':belephants,
    #         'bad':badvisors,
    #         'bge':bgeneral,
    #         'bca':bcannos,
    #         'bso':bsoiders,
    # }