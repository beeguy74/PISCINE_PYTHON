#!/usr/bin/env python3

from ft_calculator import calculator


def prYellow(skk):
    """prints to stdout in yellow color"""
    print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk):
    """prints to stdout in green color"""
    print("\033[92m {}\033[00m" .format(skk))


def main():
    """my tests"""
    prYellow('\n00 test from subject')
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
