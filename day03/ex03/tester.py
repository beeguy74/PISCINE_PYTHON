#!/usr/bin/env python3

from ft_calculator import calculator


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    prYellow("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    prYellow("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5

    prYellow('\n01 0 division')
    try:
        v3 / 0
    except AssertionError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
