from load_csv import load


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    print(load("sample_data/life_expectancy_years.csv"))

    prYellow('\n01 wrong filename')
    print(load("landscape"))

    prYellow('\n03 dir')
    print(load("sample_data"))


if __name__ == "__main__":
    main()
