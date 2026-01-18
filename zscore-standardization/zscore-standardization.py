import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    X = np.array(X)
    mean = np.mean(X , axis=axis, keepdims=True )                       # across each_coln
    std_dev = np.std(X , axis = axis , keepdims=True)

    # print(std_dev)
    # print(mean)

    ans = (X - mean) / np.maximum(std_dev,eps)
    
    return ans









