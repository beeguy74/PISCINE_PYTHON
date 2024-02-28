import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    ''' takes as parameters a 2D array, prints its shape, and returns a
        truncated version of the array based on the provided start
        and end arguments.'''
    res = []
    try:
        res = family[start:end]
        print("My shape is :", np.shape(family))
        print("My new shape is :", np.shape(res))
    except Exception as e:
        print("Error slice_me:", e)
    return res
