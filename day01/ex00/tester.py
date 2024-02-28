from give_bmi import give_bmi, apply_limit


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    prGreen(f"{bmi} {type(bmi)}")
    prGreen(apply_limit(bmi, 26))

    prYellow('\n01 string on 1 list')
    height = [2.71, '2.71']
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    prGreen(f"{bmi} {type(bmi)}")
    prGreen(apply_limit(bmi, 26))

    prYellow('\n02 string on 2 list')
    height = [2.71, 2.71]
    weight = [165.3, '38.4']
    bmi = give_bmi(height, weight)
    prGreen(f"{bmi} {type(bmi)}")
    prGreen(apply_limit(bmi, 26))

    prYellow('\n03 wrong size of 1 list')
    height = [2.71]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    prGreen(f"{bmi} {type(bmi)}")
    prGreen(apply_limit(bmi, 26))

    prYellow('\n04 wrong size of 2 list')
    height = [2.71, 2.71]
    weight = [165.3]
    bmi = give_bmi(height, weight)
    prGreen(f"{bmi} {type(bmi)}")
    prGreen(apply_limit(bmi, 26))

    prYellow('\n06 wrong args give_bmi')
    height = [2.71, 1.15]
    weight = 2
    bmi = give_bmi(height, weight)
    prGreen(f"{bmi} {type(bmi)}")
    prGreen(apply_limit(bmi, 26))

    prYellow('\n07 wrong args apply_limit')
    bmi = [2.71, 1.15]
    prGreen(apply_limit(bmi, 'sa'))

    prYellow('\n08 wrong args apply_limit')
    bmi = []
    prGreen(apply_limit(bmi, -1))

    prYellow('\n09 wrong args apply_limit')
    bmi = 'as'
    prGreen(apply_limit(bmi, -1))

    prYellow('\n10 wrong args apply_limit')
    bmi = [1, 's']
    prGreen(apply_limit(bmi, -1))

    prYellow('\n11 wrong args apply_limit')
    bmi = [2.71, 1.15]
    prGreen(apply_limit(bmi, 1.1))


if __name__ == "__main__":
    main()
