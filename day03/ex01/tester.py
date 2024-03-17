#!/usr/bin/env python3

from S1E7 import Baratheon, Lannister


def prYellow(skk):
    """prints to stdout in yellow color"""
    print("\033[93m {}\033[00m" .format(skk))


def prGreen(skk):
    """prints to stdout in green color"""
    print("\033[92m {}\033[00m" .format(skk))


def main():
    """my tests"""
    prYellow('\n00 test from subject')
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
