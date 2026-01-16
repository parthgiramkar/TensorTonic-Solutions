import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    n = len(y_pred)
    ans = (y_pred - y_true)**2
    summ = np.sum(ans)

    return np.sum(ans)/y_true.shape[0]                  # this also_works -_-
