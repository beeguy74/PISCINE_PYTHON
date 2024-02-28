import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    ''' takes as parameters a 2D array, prints its shape, and returns a
        truncated version of the array based on the provided start
        and end arguments.'''
    try:
        numpyArray = np.array(family)
        assert len(numpyArray.shape) == 2, "first arg isn't a 2d list!"
        assert isinstance(start, int), "second arg isn't an int"
        assert isinstance(end, int), "end arg isn't an int"
        res = numpyArray[start:end]
        print("My shape is :", numpyArray.shape)
        print("My new shape is :", res.shape)
        return res.tolist()
    except Exception as e:
        print("Error slice_me:", e)
    return []
