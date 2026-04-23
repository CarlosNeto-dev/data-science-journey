"""Exercise 02 - Character Sets"""

import re

def extract_a_b_grades(text):
    """
    Extracts all 'A' and 'B' grades.

    :param text: String of grades
    :return: List of Matches
    """

    return re.findall(r"[AB]", text)


def main():
    """Main program execution"""

    grades = "ABACBBACCA"

    print(extract_a_b_grades(grades))


if __name__ == "__main__":
    main()
