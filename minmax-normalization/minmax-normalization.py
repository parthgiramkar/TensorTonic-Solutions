import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X= np.array(X,dtype=float)
    min = np.min(X,axis=axis,keepdims=True)
    max = np.max(X,axis=axis,keepdims=True)
    # print(max)
    # print(min)

    ans = (X - min) / np.where(max == min , eps , max-min)
    return ans