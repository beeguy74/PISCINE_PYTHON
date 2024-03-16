#!/usr/bin/env python3

from S1E9 import Character, Stark


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    prYellow('\n00 test from subject')
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    prYellow("\n01 trying to create an Character's instance")
    try:
        hodor = Character("hodor")
        print(hodor.__dict__)
    except TypeError as e:
        print("TypeError: ", e)


if __name__ == "__main__":
    main()
