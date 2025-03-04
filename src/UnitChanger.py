import numpy as np
from dfexception import NotSimplfiedException
BoundaryLength=31
BlockLength=(429-2*BoundaryLength)//8
def PF(pos):
    "Position Fixer"
    return (pos-BoundaryLength//BlockLength)*BlockLength
def PTM(x,y)->tuple:
    "Position to Matrix"
    if (x-BoundaryLength)%BlockLength!=0 or (y-BoundaryLength)%BlockLength!=0:
        raise NotSimplfiedException('Not Simplified')
    else:
        return (y-BoundaryLength)//BlockLength+1,(x-BoundaryLength)//BlockLength+1
def MTP(y,x)->tuple:
    "Matrix to Position"
    return (y+1)*BlockLength+BoundaryLength,(x+1)*BlockLength+BoundaryLength