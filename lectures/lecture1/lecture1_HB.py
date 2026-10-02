"""
Part 2, Lecture 1

Implement and test an argmax() function that returns the location of a maximum.

Tasks
-----

1.  Implement a function argmax() that takes a sequence of numbers and returns
    the index (position) of the maximum element.

2.  Test the function with the following sequence of numbers:
    [2, 3, -1, 7, 4]

3.  Add error handling if an empty sequence is passed. Test the function with an
    empty sequence.

4.  Use the notebook lecture1.ipynb to benchmark your implementation
    against NumPy's argmax().
"""

import numpy as np


def argmax(values):
    """
    Return the index of the maimum value in a collect.

    Parameters
    ------
    Values
        Sequence of values
    Return
    ------
    imax: int
        Index of maximum
    """
    N = len(values)

    imax = None
    # set vmax to lowest possible value:
    vmax = -np.inf

    for i in range(N):
        # first iteration: value = 2
        value = values[i]
        # check whether this value is larger than any previous
        if value > vmax:
            # Update index and vma
            vmax = value
            imax = i

    return imax

if __name__ == '__main__':
    values = [2, 3, -1, 7, 4]
    imax = argmax(values)
    print(imax)


    #Compare to Numpys argmax
    j = np.argmax(values)
    print(j)