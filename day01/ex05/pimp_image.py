import numpy as np


def ft_invert(array: np.array) -> np.array:
    '''invert colors of given image array'''
    res = np.full(array.shape, 255, dtype=np.uint8)
    res -= array
    return res


def ft_red(array: np.array) -> np.array:
    """apply red filter"""
    res = np.full(array.shape, (1, 0, 0), dtype=np.uint8)
    res *= array
    return res


def ft_green(array: np.array) -> np.array:
    """apply green filter"""
    res = np.copy(array)
    res[:, :, 0] -= array[:, :, 0]
    res[:, :, 2] -= array[:, :, 2]
    return res


def ft_blue(array: np.array) -> np.array:
    """apply blue filter"""
    res = np.zeros_like(array, dtype=np.uint8)
    res[:, :, 2] = array[:, :, 2]
    return res


def ft_grey(array: np.array) -> np.array:
    """apply grayscale filter"""
    r_ch = array[:, :, 0] / 3
    g_ch = array[:, :, 1] / 3
    b_ch = array[:, :, 2] / 3
    grey = r_ch + g_ch + b_ch
    res = np.stack([grey, grey, grey], axis=2)
    return res.astype(np.uint8)
