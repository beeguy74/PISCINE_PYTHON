import sys as sys
from ft_filter import ft_filter


def filterstring(args) -> int:
    """
    output a list of words from args[1] that have a length
    greater than number in args[2].
    """
    number = 0
    try:
        number = int(args[2])
    except BaseException:
        raise AssertionError("the arguments are bad")
    words = args[1].split()
    res = ft_filter(
        lambda x: len(x) > number,
        words
    )
    print(*[resWord for resWord in res])
    return 0


def main() -> int:
    """
    handling an assertion error and run the filterstring programm
    """
    args = sys.argv
    try:
        assert len(args) == 3, "the arguments are bad"
        filterstring(sys.argv)
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
        return 1
    return 0


if __name__ == "__main__":
    main()
