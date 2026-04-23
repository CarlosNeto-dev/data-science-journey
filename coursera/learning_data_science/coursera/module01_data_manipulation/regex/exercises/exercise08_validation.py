"""Exercise 08 - Email Validation"""

import re

def is_valid_email(email):
    """
    Validates an Email Address

    :param email: Input String
    :return: Boolean Result
    """

    pattern = r"""
    (?P<username>[a-zA-Z0-9]+(?:[._][a-zA-Z0-9]+)*)
    @
    (?P<domain>[a-zA-Z0-9]+)
    [.]
    (?P<extension>[\w]{2,4}(?:[.][\w]{2})?)
    $
    """

    return bool(re.search(pattern, email, re.VERBOSE))


def main():
    """Main program execution"""

    print(is_valid_email("netoc222@gmail.com"))
    print(is_valid_email("carlos_123@gmail.com.br"))
    print(is_valid_email("pedro.araujo@yahoo.com.br"))
    print(is_valid_email("carlos..@gmail.com"))
    print(is_valid_email("maria_de_santos@hotmail..com.br"))


if __name__ == "__main__":
    main()
