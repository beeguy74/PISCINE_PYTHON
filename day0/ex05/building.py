import sys as sys


def is_punctuation(char):
    """return True if char is a punctuation symbol"""
    return char in r"""#$%&'()*+,-./:;<=>?@[\]^_`{|}!"~"""


def test() -> str:
    """this function can read stdin with carriage returns and detect ctrl+d"""
    msg = ""
    print("What is the text to count?")
    for line in sys.stdin:
        msg += line
    return msg


def count(args) -> int:
    """
    takes a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters,
    digits and spaces.
    """
    funcMap = {
        "upper letters": str.isupper,
        "lower letters": str.islower,
        "punctuation marks": is_punctuation,
        "spaces": str.isspace,
        "digits": str.isdigit
    }
    text = test() if len(args) != 2 else args[1]
    print(f"The text contains {len(text)} characters:")
    for name, func in funcMap.items():
        res = 0
        for char in text:
            res += 1 if func(char) else 0
        print(res, name)
    return res


def main() -> int:
    """
    handling an sassertion error and run the count programm
    """
    args = sys.argv
    try:
        assert 0 < len(args) < 3, "more than one argument is provided"
        count(args)
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
        return 1
    return 0


if __name__ == "__main__":
    main()
