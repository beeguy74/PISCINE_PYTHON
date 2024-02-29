import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    ''' loads an image, prints its format, and its pixels
    content in RGB format.'''
    data = np.array([])
    try:
        with Image.open(path) as f:
            data = np.array(f)
            print("The shape of image is: ", np.shape(data))
            print(data)
            return data
    except Exception as e:
        print("Error ft_load:", e)
    return data
