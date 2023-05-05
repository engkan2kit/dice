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

def generateDieRoll(n):
    """
    This function generates an array of random integer ranging
    ranging from to 6.

    usage: generateDieRoll(3) 
    returns: list with 3 random values
    """
    result = []
    for i in range(n):
        result.append(random.randint(1,6))
    return result
