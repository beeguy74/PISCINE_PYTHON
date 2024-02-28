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

    prYellow('\n01 string on 1 list')

    prYellow('\n02 string on 2 list')

    prYellow('\n03 wrong size of 1 list')

    prYellow('\n04 wrong size of 2 list')

    prYellow('\n06 wrong args give_bmi')

    prYellow('\n07 wrong args apply_limit')

    prYellow('\n08 wrong args apply_limit')

    prYellow('\n09 wrong args apply_limit')

    prYellow('\n10 wrong args apply_limit')

    prYellow('\n11 wrong args apply_limit')


if __name__ == "__main__":
    main()
