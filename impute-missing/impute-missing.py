import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    x = np.array(X,dtype=float,copy=True)
    
    import warnings
    if np.size(x) == 0 or np.all(np.isnan(x))  :             # np.all() ,Returns True if all element is True

        ans = np.where(np.isnan(x) , 0 , x )
        return ans

    if np.ndim(x) == 0 :
        
        return np.array(0.0)

    with warnings.catch_warnings():
        # Suppress "Mean of empty slice" or "All-NaN slice" warnings
        warnings.simplefilter("ignore", category=RuntimeWarning)

        if strategy == 'mean' :

            strategy_val = np.nanmean(x,axis=0,keepdims=True)             #  mean of array elements while ignoring NaN values
            #print(strategy_val)

        else :

            strategy_val = np.nanmedian(x,axis=0,keepdims=True)
            #print(strategy_val)


    ans = np.where(np.isnan(x) , strategy_val , x)
    #print(ans)

    res = np.where(np.isnan(ans) , 0 , ans)
    return res



