'This is the center of the sprites'
from tool.UnitChanger import *
import numpy as np
import pygame
from asserts.images.images import *
from tool.Constants import r
from math import floor
screen=pygame.display.set_mode(ScreenSize)
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
Dict={
            'rch':rchariots,
            'rho':rhorses,
            'rel':relephants,
            'rad':radvisors,
            'rge':rgeneral,
            'rca':rcannos,
            'rso':rsoiders,
            'bch':bchariots,
            'bho':bhorses,
            'bel':belephants,
            'bad':badvisors,
            'bge':bgeneral,
            'bca':bcannos,
            'bso':bsoiders,
    }
class Runner:
    def red(self):
        self.side='r'
        self.antiside='b'
        return self
    def black(self):
        self.side='b'
        self.antiside='r'
        return self
    def ch(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        a='''
        while Matrix[i][j] in Dict:
            i+={m}
            j+={n}
            x,y=MTP(i,j)
            print(x,y)
            self.l.append((x,y))
        if ('self.antiside'==Matrix[i+{m}][j+{n}][0] 
        and {s}):
            x,y=MTP(i+{m},j+{n})
            print(x,y)
            self.l.append((x,y))
           
        '''
        exec(a.format(m=1,n=0,s='i+1<=9'))
        exec(a.format(m=-1,n=0,s='i-1>=0'))
        exec(a.format(m=0,n=1,s='j+1<=8'))
        exec(a.format(m=0,n=-1,s='j-1>=0'))
        return self
    
    def ho(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
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
        if Matrix[i+{m}][j+{n}] not in Dict:
            if ((a:=Matrix[i+{m}+d2[(m,n)][0][1]][j+{n}+d2[(m,n)][0][0]]) 
            and a[0]==self.antiside 
            or a=='000'):
                x,y=MTP(i+{m}+d2[(m,n)][0][1],j+{n}+d2[(m,n)][0][0])
                print(x,y)
                self.l.append((x,y))
            if ((b:=Matrix[i+{m}+d2[(m,n)][1][1]][j+{n}+d2[(m,n)][1][0]]) 
            and b[0]==self.antiside 
            or b=='000'):
                x,y=MTP(i+{m}+d2[(m,n)][1][1],j+{n}+d2[(m,n)][1][0])
                print(x,y)
                self.l.append((x,y))
        '''
        exec(a.format(m=1,n=0))
        exec(a.format(m=-1,n=0))
        exec(a.format(m=0,n=1))
        exec(a.format(m=0,n=-1))
        return self
    
    def el(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        a='''
        lim:int
        match i:
            case 0|1|2|3|4:
                lim=5
            case 5|6|7|8|9:
                lim=9
        if Matrix[i+{m}][j+{n}] not in Dict:
            if ((s:=Matrix[i+{m}+{m}][j+{n}+{n}]) not in Dict 
            or s[0]==self.antiside 
            and lim-5<=i+{m}+{m}<=lim):
                x,y=MTP(i+{m}+{m},j+{n}+{n})
                self.l.append((x,y))       
        '''
        exec(a.format(m=1,n=0))
        exec(a.format(m=-1,n=0))
        exec(a.format(m=0,n=1))        
        exec(a.format(m=0,n=-1))
        return self
    
    def ad(self,position:tuple):  #士
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        match i:
            case 0|1|2:
                limj = 2
                limi = 0
            case 7|8|9:
                limj = 9
                limi = 7
        move=[(1,1),(-1,-1),(-1,1),(1,-1)]
        for m,n in move:
             new_i, new_j = i + m, j + n
             if 0 <=new_i< Matrix.shape[0] and 0 <= new_j < Matrix.shape[1]:
                target = Matrix[new_i][new_j]
                if ((target not in Dict 
        or self.antiside==target[0]) 
        and (limi<=new_i<=limj)):
                    x,y=MTP(new_i,new_j)
                    print(x,y)
                    self.l.append((x,y))
        return self
    
    def ge(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        a='''
        match floor(i/5):
            case 0:
                limj=(...)
                limi=(...)
            case 1:
                limj=(...)
                limi=(...)
        if (Matrix[i+{m}][j+{n}] not in Dict
        or self.antiside==Matrix[i+{m}][j+{n}][0]):
            ...
        '''
        return self
    def ca(self,position:tuple):
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        a='''
        while Matrix[i][j] not in Dict:
            i+={m}
            j+={n}
            x,y=MTP(i,j)
            print(x,y)
            self.l.append((x,y))
        while 0<=i<=9 and 0<=j<=8: 
            i+={m}
            j+={n}         
    '''
        return self
    def so(self,position:tuple):
        ...
        return self
    def PrePrint(self):
        for li in self.l:
            screen.blit(preon,li)
    def __init__(self):
        self.r=self.red()
        self.b=self.black()
runner=Runner()
RunDict={
            'rch':runner.r.ch,
            'rho':runner.r.ho,
            'rel':runner.r.el,
            'rad':runner.r.ad,
            'rge':runner.r.ge,
            'rca':runner.r.ca,
            'rso':runner.r.so,
            'bch':runner.b.ch,
            'bho':runner.b.ho,
            'bel':runner.b.el,
            'bad':runner.b.ad,
            'bge':runner.b.ge,
            'bca':runner.b.ca,
            'bso':runner.b.so, 
}
class Center:
    def init(self):
        'To initialize the chessboard'
        for i in range(len(Matrix)):
            for j in range(len(Matrix[i])):
                if Matrix[i][j] in Dict:
                    screen.blit(Dict[Matrix[i][j]],MTP(i,j))
                    print(MTP(i,j),Matrix[i][j])
    def check(self,mospos:tuple):
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                if (m:=Matrix[*PTM(*PF(mospos))]) != '000':
                    print(m,PTM(*PF(mospos)))
                    Dict[m]=pygame.transform.scale(Dict[m],(1.5*r[0],1.5*r[1]))
                    screen.blit(Dict[m],mospos)
                    RunDict[m](mospos).PrePrint()
                else:
                    Dict[m]=pygame.transform.scale(Dict[m],(r[0],r[1]))
                    screen.blit(Dict[m],mospos)
    def run(self,mospos:tuple):

        ...
center=Center()