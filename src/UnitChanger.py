import numpy as np
from .dfexception import NotSimplfiedException
#<constants>
BoundaryLength=20
OriginalBoardSize=(185,205)
BlockLength=(OriginalBoardSize[0]*2-BoundaryLength)//8
r=(BlockLength,BlockLength)
sigma_yi_=12
sigma_xj_=26
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
    return (j)*BlockLength+BoundaryLength-sigma_xj_,(i)*BlockLength-sigma_yi_