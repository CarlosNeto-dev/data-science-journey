"""Exercise 07 - Data Cleaning"""

import re

def clean_text(text):
    """
    Remove special characters from the text

    :param text: Input String
    :return: Cleaned Text
    """

    return re.sub(r"[^\w\s]", "", text)


def main():
    """Main program execution"""

    text = "Data@Science! is #powerful."

    print(clean_text(text))


if __name__ == "__main__":
    main()
