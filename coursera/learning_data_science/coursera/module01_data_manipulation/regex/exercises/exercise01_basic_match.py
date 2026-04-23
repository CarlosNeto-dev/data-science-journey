"""Exercise 01 - Basic Regex Match"""

import re

def find_word_data(text):
    """
    Find all occurrences of word "data" in given text

    :param text: Text to be searched
    :return: List of Matches
    """

    return re.findall(r"data", text)


def main():
    """Main program execution"""

    text = "data science uses data for data-driven decisions"

    print(find_word_data(text))


if __name__ == "__main__":
    main()
