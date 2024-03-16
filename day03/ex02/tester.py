#!/usr/bin/env python3

from DiamondTrap import King


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

    prYellow('\n01 property')
    print(Joffrey.eyes.__doc__)


if __name__ == "__main__":
    main()
