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


def ft_transpose(matrix: np.ndarray) -> np.ndarray:
    '''rotates matrix 90 degrees to the left'''
    res = np.empty(matrix.shape, dtype=np.uint8)
    for i, line in enumerate(zip(*matrix)):
        res[i] = np.array(line, dtype=np.uint8)
    return res


def main():
    '''
    load the image "animal.jpeg", print some information
    about it and display it after "zooming".
    '''
    try:
        file = ft_load("animal.jpg")
        assert len(file) > 0, 'image not found'
    except Exception as e:
        print("Error load:", e)
    try:
        zoomd = ft_zoom(file, (-601, -201), (-501, -101), (1, 2))
        zoomd_sh = zoomd.squeeze()
        print(f"The shape of image is: {zoomd.shape} or {zoomd_sh.shape}")
        print(zoomd)
    except Exception as e:
        print("Error zoom:", e)
    try:
        res = ft_transpose(zoomd_sh)
        print(f'New shape after Transpose: {res.shape}')
        print(res)
        plt.imshow(res, cmap='gray')
        plt.show()
    except Exception as e:
        print("Error transpose:", e)


if __name__ == "__main__":
    main()
