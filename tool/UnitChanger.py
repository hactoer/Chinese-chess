import numpy as np
from .dfexception import NotSimplfiedException
from .Constants import *
from math import *
def PF(pos:tuple)->tuple:
    "Position Fixer"
    return ((pos[0]-BoundaryLength)//BlockLength)*BlockLength,((pos[1]-BoundaryLength)//BlockLength)*BlockLength
def PTM(x,y)->tuple:
    "Position to Matrix(x,y)->(i,j)"
    data=[((x - BoundaryLength + sigma_xj_) / mul_xj_),
          ((y -BoundaryLength+ sigma_yi_) / mul_yi_)]
    
    if abs(data[0]-round(data[0]))>.5  or abs(data[1]-round(data[1]))>.5:
        raise NotSimplfiedException('Not Simplified',data)
    else:
        return (y-BoundaryLength)//BlockLength,(x-BoundaryLength)//BlockLength
def MTP(i,j)->tuple:
    "Matrix to Position(i,j)->(x,y)"
    return mul_xj_*(j)*BlockLength+BoundaryLength-sigma_xj_,mul_yi_*(i)*BlockLength-sigma_yi_