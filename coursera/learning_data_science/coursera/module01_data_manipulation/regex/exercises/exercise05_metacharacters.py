"""Exercise05 - Metacharacters"""

import re

def extract_numbers(text):
    """
    Extract all numbers from text

    :param text: Input String
    :return: List of numbers
    """

    return re.findall(r"\d+", text)


def main():
    """Main program execution"""

    text = "Order 123 costs 45 dollars and 6 cents"

    print(extract_numbers(text))


if __name__ == "__main__":
    main()
