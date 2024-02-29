from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from load_image import ft_load
import matplotlib.pyplot as plt


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    try:
        file = ft_load("landscape.jpg")
        assert len(file) > 0, 'image not found'
    except Exception as e:
        print("Error load:", e)

    prYellow('\n00 inverted colors')
    inverted = ft_invert(file)
    plt.imshow(inverted)
    plt.show()
    plt.clf()

    prYellow('\n01 red filter')
    reded = ft_red(file)
    plt.imshow(reded)
    plt.show()
    plt.clf()

    prYellow('\n02 green filter')
    greened = ft_green(file)
    plt.imshow(greened)
    plt.show()
    plt.clf()

    prYellow('\n03 blue filter')
    blued = ft_blue(file)
    plt.imshow(blued)
    plt.show()
    plt.clf()

    prYellow('\n04 gryy filter')
    greied = ft_grey(file)
    print(greied)
    plt.imshow(greied)
    plt.show()
    plt.clf()


if __name__ == "__main__":
    main()
