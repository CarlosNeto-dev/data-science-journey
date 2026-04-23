"""Exercise 04 - Quantifiers"""

import re

def find_multiple_letter_a(text):
    """
    Finds sequences of one or more 'A'.

    :param text: Input String
    :return: List of Matches
    """

    return re.findall(r"A+", text)


def main():
    """Main program execution"""

    text = "BAAACDAAFAA"

    print(find_multiple_letter_a(text))


if __name__ == "__main__":
    main()
