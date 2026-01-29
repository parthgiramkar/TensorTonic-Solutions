import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x)

    # mean = np.mean(x)
    # median = np.median(x)
    # values , counts = np.unique(x,return_counts=True)           # sorted unique elements of an array

    # mode = values[np.argmax(counts)]                        #  indices of the maximum value
    # return mean , median , mode 


    
 #   .most_common() List- the n most common(freq) elements and their counts

    mode = Counter(x).most_common(1)[0][0]         # getting the most_freq/common_element-value
    mean = np.mean(x)
    median = np.median(x)
    return mean , median , mode 















    