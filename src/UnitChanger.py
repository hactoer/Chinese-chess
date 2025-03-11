import numpy as np
from .dfexception import NotSimplfiedException
BoundaryLength=20
BlockLength=(185*2-BoundaryLength)//8
r=(BlockLength,BlockLength)
def PF(pos:tuple)->tuple:
    "Position Fixer"
    return ((pos[0]-BoundaryLength)//BlockLength)*BlockLength,((pos[1]-BoundaryLength)//BlockLength)*BlockLength
def PTM(x,y)->tuple:
    "Position to Matrix(x,y)->(i,j)"
    if (x-BoundaryLength)%BlockLength!=0 or (y-BoundaryLength)%BlockLength!=0:
        raise NotSimplfiedException('Not Simplified')
    else:
        return (y-BoundaryLength)//BlockLength,(x-BoundaryLength)//BlockLength
def MTP(i,j)->tuple:
    "Matrix to Position(i,j)->(x,y)"
    return (j)*BlockLength+BoundaryLength,(i)*BlockLength