from load_image import ft_load


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    print(ft_load("landscape.jpg"))

    prYellow('\n01 wrong filename')
    print(ft_load("landscape"))

    prYellow('\n02 wrong rights')
    print(ft_load("sample_data/landscape_1.jpg"))

    prYellow('\n03 dir')
    print(ft_load("sample_data"))

    prYellow('\n04 image_corrupted')
    print(ft_load("sample_data/landscape_corrupted.jpg"))


if __name__ == "__main__":
    main()
