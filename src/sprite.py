# -*- coding: utf-8 -*-
'This is the center of the sprites'
from tool.UnitChanger import *
import numpy as np
import pygame
from asserts.images.images import *
from tool.Constants import r
from math import floor
from tool.dfexception import *
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
    def el(self,position:tuple):#象
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        move=[(1,1),(-1,1),(1,-1),(-1,-1)]
        for m,n in move:
                        # if i <= 4:
            #     lim = 5
            # else:
            #     lim = 9
            detect_i,detect_j=i+m,j+n
            new_i,new_j=i+2*m,j+2*n
            if 0<=new_i<=9 and 0<=new_j<=8:
                if Matrix[detect_i][detect_j]=="000":     #沒被塞象眼
                    if (self.antiside == 'r' and new_i <= 4 or 
                        self.antiside == 'b' and new_i >= 5):
                        if (Matrix[new_i][new_j]=="000" 
                        or Matrix[new_i][new_j][0]==self.antiside): #空or敵對
                    # if ((s:=Matrix[new_i][new_j]) =="000"
                    # or s[0]==self.antiside 
                    # and lim-5<=new_i<=lim):
                            x,y=MTP(new_i,new_j)
                            self.l.append((x,y))      
        return self

    def ch(self,position:tuple):#車
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        move=[(1,0),(-1,0),(0,1),(0,-1)]
        for m,n in move:
            new_i=i+m
            new_j=j+n
            while 0<=new_i<=9 and 0<=new_j<=8:
                x,y=MTP(i,j)
                print(x,y)
                self.l.append((x,y))
                if (self.antiside==Matrix[i+m][j+n][0] 
                and s):
                    x,y=MTP(i+m,j+n)
                    print(x,y)
                    self.l.append((x,y))
        return self
    
    def ho(self,position:tuple):#馬
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
        move=[(1,0),(-1,0),(0,1),(0,-1)]
        for m,n in move:

            if Matrix[i+m][j+n] not in Dict:
                if ((a:=Matrix[i+m+d2[(m,n)][0][1]][j+n+d2[(m,n)][0][0]]) 
                and a[0]==self.antiside 
                or a=='000'):
                    x,y=MTP(i+m+d2[(m,n)][0][1],j+n+d2[(m,n)][0][0])
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        move=[(1,1),(-1,1),(1,-1),(-1,-1)]
        for m,n in move:
            # if i <= 4:
            #     lim = 5
            # else:
            #     lim = 9
            detect_i,detect_j=i+m,j+n
            new_i,new_j=i+2*m,j+2*n
            if 0<=new_i<=9 and 0<=new_j<=8:
                if Matrix[detect_i][detect_j]=="000":     #沒被塞象眼
                    if (self.antiside == 'r' and new_i <= 4 or 
                        self.antiside == 'b' and new_i >= 5):
                        if (Matrix[new_i][new_j]=="000" 
                        or Matrix[new_i][new_j][0]==self.antiside): #空or敵對
                    # if ((s:=Matrix[new_i][new_j]) =="000"
                    # or s[0]==self.antiside 
                    # and lim-5<=new_i<=lim):
                            x,y=MTP(new_i,new_j)
                            self.l.append((x,y))      
        return self

    def ad(self,position:tuple):  #士
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        if self.antiside=="r":
            limj = 2
            limi = 0
        elif self.antiside=="b":
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

    def ge(self,position:tuple):#將
        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        move=[(1,0),(-1,0),(0,1),(0,-1)]
        if self.antiside=="b":
            lim_i=range(7,10)
        elif self.antiside=="r":
            lim_i=range(0,3)
        else:
            raise OutSideTheLimit('not in chessboard')
        lim_j=range(3,6)
        for m,n in move:
            new_i=i+m
            new_j=j+n
            if new_i in lim_i and new_j in lim_j:
                if (Matrix[new_i][new_j] not in Dict
                or self.antiside==Matrix[new_i][new_j][0]):
                    self.l.append((new_i,new_j))
        return self
    def ca(self,position:tuple):#砲
        x,y=PF(position)
        i,j=PTM(x,y)#i=y j=x
        self.l=[]
        move=[(1,0),(-1,0),(0,1),(0,-1)]
        for m,n in move:
            found_obstacle=False
            ni=i+n
            nj=j+m
            while 0 <= ni <= 8 and 0 <= nj <= 9:
                
                if not found_obstacle:
                    if Matrix[ni][nj]=="000":
                        x1,y1=MTP(ni,nj)
                        self.l.append((x1,y1))#可移動的格子
                    else:
                        found_obstacle=True
                else:
                    if Matrix[ni][nj]!="000":
                        if self.antiside==Matrix[ni][nj][0]:
                            x1,y1=MTP(ni,nj)
                            self.l.append((x1,y1))
                        break#無論能不能吃，都得暫停(因為已經找到第二個)
                ni+=n
                nj+=m
                print(x,y)
        return self
    def so(self,position:tuple):#兵
        x,y=PF(position)
        i,j=PTM(x,y)#i=y j=x
        self.l=[]
        

        x,y=PF(position)
        i,j=PTM(x,y)
        self.l=[]
        if self.antiside == "b":  # 黑方：往下走（+1）
            forward = 1
            crossed_river = i >= 5
        elif self.antiside == "r":  # 紅方：往上走（-1）
            forward = -1
            crossed_river = i <= 4
        else:
            raise OutSideTheLimit('not in chessboard')
        
        new_i, new_j = i + forward, j
        if 0 <= new_i <= 9 and 0 <= new_j <= 8:
            target = Matrix[new_i][new_j]
        if target == '000' or target[0] == self.antiside:
            self.l.append(MTP(new_i, new_j))
        if crossed_river:
            for dj in [-1, 1]:
                new_i, new_j = i, j + dj
                if 0 <= new_i <= 9 and 0 <= new_j <= 8:
                    target = Matrix[new_i][new_j]
                    if target == '000' or target[0] == self.antiside:
                        self.l.append(MTP(new_i, new_j))
        return self
    def PrePrint(self):
        for li in self.l:
            screen.blit(preon,li)
    def __init__(self):
        self.r=self.red()
        self.b=self.black()
        self.dragging = False
        self.drag_piece = None
        self.drag_offset = (0, 0)
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
    def check(self,mospos:tuple):
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                pos=PTM(*PF(mospos))
                if (m:=Matrix[*pos]) != '000':
                    print(m,PTM(*PF(mospos)))
                    self.dragging = True                    # 設定為正在拖曳
                    self.drag_piece = m                     # 儲存正在拖的棋子代號
                    piece_rect = Dict[m].get_rect(topleft=mospos)
                    self.drag_offset = (mospos[0] - piece_rect.x, mospos[1] - piece_rect.y) 
                    # 保留移動預覽提示
                    RunDict[m](mospos).PrePrint()
                else:
                    Dict[m]=pygame.transform.scale(Dict[m],(r[0],r[1]))
                    screen.blit(Dict[m],mospos)
    def run(self, mospos: tuple):
        if self.dragging and self.drag_piece:
             # 計算棋子應該畫在哪裡（讓滑鼠點始終維持在棋子內部）
            new_pos = (mospos[0] - self.drag_offset[0], mospos[1] - self.drag_offset[1])
             # 放大棋子顯示（拖曳時常用）
            scaled_img = pygame.transform.scale(Dict[self.drag_piece], (int(1.5*r[0]), int(1.5*r[1])))
            # 繪製到畫面上
            screen.blit(scaled_img, new_pos)
    def detect_general():
        ...
center=Center()  