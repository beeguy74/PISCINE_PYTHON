import sys as sys


def morse(text) -> int:
    """takes a string as an argument and prints it into Morse Code"""
    NESTED_MORSE = {'A': '.- ',     'B': '-... ',   'C': '-.-. ',
                    'D': '-.. ',    'E': '. ',      'F': '..-. ',
                    'G': '--. ',    'H': '.... ',   'I': '.. ',
                    'J': '.--- ',   'K': '-.- ',    'L': '.-.. ',
                    'M': '-- ',     'N': '-. ',     'O': '--- ',
                    'P': '.--. ',   'Q': '--.- ',   'R': '.-. ',
                    'S': '... ',    'T': '- ',      'U': '..- ',
                    'V': '...- ',   'W': '.-- ',    'X': '-..- ',
                    'Y': '-.-- ',   'Z': '--.. ',
                    '0': '----- ',  '1': '.---- ',  '2': '..--- ',
                    '3': '...-- ',  '4': '....- ',  '5': '..... ',
                    '6': '-.... ',  '7': '--... ',  '8': '---.. ',
                    '9': '----. '
                    }
    res = ""
    for word in text.split():
        if not word.isalnum():
            raise AssertionError("the arguments are bad")
        morseWord = "".join([NESTED_MORSE[char.capitalize()]
                            for char in word])
        morseWord += "/ "
        res += morseWord
    print(res[:-3])
    return 0


def main() -> int:
    """ takes a string in an args[1] and encodes it into Morse Code"""
    args = sys.argv
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        morse(args[1])
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
        return 1
    return 0


if __name__ == "__main__":
    main()
