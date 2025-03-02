import numpy as np
from dexception import NotSimplfiedException
BoundaryLength=31
BlockLength=(429-2*BoundaryLength)//8
def PF(pos):
    "Position Fixer"
    return (pos-BoundaryLength//BlockLength)*BlockLength
def PTM(x,y):
    "Position to Matrix"
    if (x-BoundaryLength)%BlockLength!=0 or (y-BoundaryLength)%BlockLength!=0:
        raise NotSimplfiedException('Not Simplified')
    else:
        return (x-BoundaryLength)//BlockLength+1,(y-BoundaryLength)//BlockLength+1
        