import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(
        image: np.ndarray,
        lines: tuple[int, int], rows: tuple[int, int],
        pixels: tuple[int, int]
        ) -> np.ndarray:
    '''slicing image array AKA "zooming"'''
    return image[lines[0]: lines[1], rows[0]: rows[1], pixels[0]: pixels[1]]


def main():
    '''
    load the image "animal.jpeg", print some information
    about it and display it after "zooming".
    '''
    try:
        file = ft_load("animal.jpg")
        assert len(file) > 0, 'image not found'
        print(file)
        res = ft_zoom(file, (-601, -201), (-501, -101), (1, 2))
        print(f'New shape after slicing: {res.shape} or {res.shape[0: 2]}')
        print(res)
        plt.imshow(res, cmap='gray')
        plt.show()
    except Exception as e:
        print("Error zoom:", e)


if __name__ == "__main__":
    main()
