"""Exercise 06 - URL Extraction"""

import re

def extract_domains(text):
    """
    Extract Domain names from URLs

    :param text: Input String
    :return: List of Domains
    """

    pattern_for_extract_domains = r"(?:(?<=https://)|(?<=http://))[\w.]+"

    return re.findall(pattern_for_extract_domains, text)


def main():
    """Main program execution"""

    text = (
        "Visit https://google.com and"
        "https://www.bing.com for more info"
    )

    print(extract_domains(text))


if __name__ == "__main__":
    main()
