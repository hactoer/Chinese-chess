import numpy as np
from src.dfexception import NotSimplfiedException
BoundaryLength=20
BlockLength=185//8
def PF(pos:tuple):
    "Position Fixer"
    return (pos[0]-BoundaryLength//BlockLength)*BlockLength,(pos[1]-BoundaryLength)//BlockLength
def PTM(x,y)->tuple:
    "Position to Matrix(x,y)->(y,x)"
    if (x-BoundaryLength)%BlockLength!=0 or (y-BoundaryLength)%BlockLength!=0:
        raise NotSimplfiedException('Not Simplified')
    else:
        return (y-BoundaryLength)//BlockLength+1,(x-BoundaryLength)//BlockLength+1
def MTP(y,x)->tuple:
    "Matrix to Position"
    return (y)*BlockLength+BoundaryLength,(x)*BlockLength+BoundaryLength