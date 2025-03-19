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
    def ch(self,position:tuple): #???
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        a='''
        while Matrix[i][j] in sprite.Dict:
            i+={m}
            j+={n}
            x,y=MTP(i,j)
            screen.bilt(sprite.Dict[Matrix[i+{m}][j+{n}]],(x,y))
            l.append((x,y))
            print(Matrix[i+{m}][j+{n}])
        if 'self.antiside'==Matrix[i+{m}][j+{n}][0] and {s}:
            x,y=MTP(i+{m},j+{n})
            screen.bilt(sprite.Dict[Matrix[i+{m}][j+{n}]],(x,y))
            l.append((x,y))
            print(Matrix[i+{m}][j+{n}])
        '''
        exec(a.format(m=1,n=0,s='i+1<=9'))
        exec(a.format(m=-1,n=0,s='i-1>=0'))
        exec(a.format(m=0,n=1,s='j+1<=8'))
        exec(a.format(m=0,n=-1,s='j-1>=0'))
    def ho(self,position:tuple): #馬
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        d={1:(+1,+1),
           2:(-1,+1),
           3:(-1,-1),
           4:(+1,-1),
           }
        d2={(0,1):(d[1],d[2]),
            (1,0):(d[1],d[4]),
            (0,-1):(d[3],d[4]),
            (-1,0):(d[2],d[3]),
            }
        a='''
        if Matrix[i+{m}][j+{n}] not in sprite.Dict:
            if (a:=Matrix[i+{m}+d2[(m,n)][0][1]][j+{n}+d2[(m,n)][0][0]]) and a[0]==self.antiside or a=='000':
                x,y=MTP(i+{m}+d2[(m,n)][0][1],j+{n}+d2[(m,n)][0][0])
                screen.bilt(sprite.Dict[a],(x,y))
                l.append((x,y))
            if (b:=Matrix[i+{m}+d2[(m,n)][1][1]][j+{n}+d2[(m,n)][1][0]])and b[0]==self.antiside or b=='000':
                x,y=MTP(i+{m}+d2[(m,n)][1][1],j+{n}+d2[(m,n)][1][0])
                l.append((x,y))
                screen.bilt(sprite.Dict[b],(x,y))
        '''
        exec(a.format(m=1,n=0))
        exec(a.format(m=-1,n=0))
        exec(a.format(m=0,n=1))
        exec(a.format(m=0,n=-1))
    def el(self,position:tuple):#象
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        a='''
        lim:int
        match floor(i/5):
            case 0:
                lim=5
            case 1:
                lim=9
        if Matrix[i+{m}][j+{n}] not in sprite.Dict:
            if (s:=Matrix[i+{m}+{m}][j+{n}+{n}]) not in sprite.Dict or s[0]==self.antiside and lim-5<=i+{m}+{m}<=lim:
                x,y=MTP(i+{m}+{m},j+{n}+{n})
                screen.bilt(sprite.Dict[Matrix[i+{m}+{m}][j+{n}+{n}]],(x,y))
                l.append((x,y))       
        '''
        exec(a.format(m=1,n=0))
        exec(a.format(m=-1,n=0))
        exec(a.format(m=0,n=1))        
        exec(a.format(m=0,n=-1))
    def ad(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        a='''
        '''
    def ge(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        l:list
        a='''
        '''
runner=Runner()
    # Dict={
    #         'rch':(rchariots),
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
