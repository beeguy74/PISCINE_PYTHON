import sys as sys


def main(obj) -> int:
    try:
        number = int(obj)
        res = "I'm "
        res += "Odd." if number % 2 else "Even."
        print(res)
    except:
        raise AssertionError("argument is not an integer")
    return 0


if __name__ == "__main__":
    args = sys.argv
    if (len(args) == 1):
      exit()
    try:
        assert len(args) == 2, "more than one argument is provided"
        main(args[1])
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
