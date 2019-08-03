import random
import numpy as np

def generateArrangements(N):
    """
    This function accepts a number N greater than or equal to 3 
    and returns an NxN matrix containing a random arrangements 
    of integers 0-((N^2)-1).

    

    usage: generateArrangements(4) 
    returns: [[1,4,7,5], [0,2,9,11], [12,15,3,6], [13,8,10,14]]
    """
    if N<3:
        return None
    list = np.arange(N**2)
    np.random.shuffle(list)
    list=list.reshape((N,N))
    return list

