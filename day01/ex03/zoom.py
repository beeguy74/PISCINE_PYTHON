import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(image: np.ndarray) -> np.ndarray:
    ''' print some information
      about image and display it after "zooming"'''
    return image[-601:-201, -501:-101, 2]


def main():
    # your tests and your error handling
    file = ft_load("animal.jpg")
    res = ft_zoom(file)
    print(np.shape(res))
    print(res)
    plt.imshow(res, cmap="viridis", interpolation="nearest")
    plt.show()


if __name__ == "__main__":
    main()
