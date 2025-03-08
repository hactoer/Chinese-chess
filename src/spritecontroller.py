from .UnitChanger import *
from ui.screen import screen
from asserts.images.images import *
import src.sprite as sprite

Matrix=np.array([
        ['rch','rho','rel','rad','rge','rad','rel','rho','rch'],
        ['000','000','000','000','000','000','000','000','000'],
        ['000','rca','000','000','000','000','000','rca','000'],
        ['rso','000','rso','000','rso','000','rso','000','rso'],
        ['000','000','000','000','000','000','000','000','000'],
        ['000','000','000','000','000','000','000','000','000'],
        ['bso','000','bso','000','bso','000','bso','000','bso'],
        ['000','bca','000','000','000','000','000','bca','000'],
        ['000','000','000','000','000','000','000','000','000'],
        ['bch','bho','bel','bad','bge','bad','bel','bho','bch']
])

class Runner:
    def r(self):
        self.side='r'
        self.antiside='b'
        return self
    def b(self):
        self.side='b'
        self.antiside='r'
        return self
    def ch(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        a='''
        while Matrix[i][j] in sprite.Dict:
            i+={m}
            j+={n}
            screen.bilt(sprite.Dict[Matrix[i{m}][j{n}]],(x,y))
            l.append((i+{m}j+{n}))
            print(Matrix[i+{m}][j+{n}])
        if 'self.antiside'==Matrix[i+{m}][j+{n}][0] and {s}:
            screen.bilt(sprite.Dict[Matrix[i+{m}][j+{n}]],(x,y))
            print(Matrix[i+{m}][j+{n}])
        '''
        exec(a.format(m=1,n=0,s='i+1<=9'))
        exec(a.format(m=-1,n=0,s='i-1>=0'))
        exec(a.format(m=0,n=1,s='j+1<=8'))
        exec(a.format(m=0,n=-1,s='j-1>=0'))
    def ho(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        a='''
        if Matrix[i+{m}][j+{n}] not in spriteDict:
            ...
            
        
        
        '''
runner=Runner()
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
