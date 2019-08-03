import random
import numpy as np

def nameOfFunction(N):
    """
    Documentation here
    """
    if N<3:
        return None
    list = np.arange(N**2)
    np.random.shuffle(list)
    list=list.reshape((N,N))
    return list

