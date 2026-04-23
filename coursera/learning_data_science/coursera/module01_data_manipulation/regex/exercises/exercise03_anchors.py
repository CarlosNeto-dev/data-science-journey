"""Exercise 03 - Anchors"""

import re

def starts_with_user(text):
    """
    Checks if text starts with 'user_'.

    :param text: Input String
    :return: Boolean Result
    """

    return bool(re.search(r"^user_", text))


def main():
    """Main program execution"""

    print(starts_with_user("user_012"))
    print(starts_with_user("_user_012"))
    print(starts_with_user("uSER_012"))
    print(starts_with_user("U s e r _ 012"))


if __name__ == "__main__":
    main()
