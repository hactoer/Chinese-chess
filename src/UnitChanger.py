import numpy as np
from .dfexception import NotSimplfiedException
BoundaryLength=20
BlockLength=185*2//8
r=(BlockLength//2,BlockLength//2)
def PF(pos:tuple):
    "Position Fixer"
    return (pos[0]-BoundaryLength//BlockLength)*BlockLength,(pos[1]-BoundaryLength)//BlockLength
def PTM(x,y)->tuple:
    "Position to Matrix(x,y)->(i,j)"
    if (x-BoundaryLength)%BlockLength!=0 or (y-BoundaryLength)%BlockLength!=0:
        raise NotSimplfiedException('Not Simplified')
    else:
        return (y-BoundaryLength)//BlockLength+1,(x-BoundaryLength)//BlockLength+1
def MTP(x,y)->tuple:
    "Matrix to Position(i,j)->(x,y)"
    return (y)*BlockLength+BoundaryLength,(x)*BlockLength