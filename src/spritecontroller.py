from .sprite import Matrix,Dict
from .UnitChanger import *
from ui.screen import screen
print(Matrix)
class Runner:
    def r(self):
        self.side='r'
        self.antiside='b'
        return self
    def b(self):
        self.side='b'
        self.antiside='r'
        return self
    def ch(self):
        i,j=PTM(*PF(self.position))
        x,y=PF(self.position)
        l:list
        a='''
        while Matrix[i+{m}][j+{n}]!='000':
            i+={m}
            j+={n}
            screen.bilt(Dict[Matrix[i{m}][j{n}]],(x,y))
            l.append((i+{m}j+{n}))
            print(Matrix[i+{m}][j+{n}])
        if 'self.antiside'==Matrix[i+{m}][j+{n}][0] and {s}:
            screen.bilt(Dict[Matrix[i+{m}][j+{n}]],(x,y))
            print(Matrix[i+{m}][j+{n}])
        '''
        exec(a.format(m=1,n=0,s='i<=9'))
        exec(a.format(m=-1,n=0,s='i>=0'))
        exec(a.format(m=0,n=1,s='j<=8'))
        exec(a.format(m=0,n=-1,s='j>=0'))
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