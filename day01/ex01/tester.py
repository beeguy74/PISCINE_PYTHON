from array2D import slice_me


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    prGreen(slice_me(family, 0, 2))
    prGreen(slice_me(family, 1, -2))

    prYellow('\n01 list has smaller size')
    family = [1.80, 78.4]
    prGreen(slice_me(family, 0, 2))

    prYellow('\n02 list has bigger size')
    family = [[[1.80], [78.4]],
              [[2.15], [102.7]],
              [[2.10], [98.5]],
              [[1.88], [75.2]]]
    prGreen(slice_me(family, 0, 2))

    prYellow('\n03 wrong second argument')
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    prGreen(slice_me(family, None, 2))

    prYellow('\n04 wrong third arg')
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    prGreen(slice_me(family, 1, 's'))


if __name__ == "__main__":
    main()
