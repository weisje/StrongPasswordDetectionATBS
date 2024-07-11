import re


def passwordStrengthDetector(stringToTest) -> bool:
    """
    Tests passed string to determine if it is at least 8 characters long, contains both an uppercase & lowercase character, and has at least one digit.
    :param stringToTest: value that will be tested for criteria of a strong password
    :type stringToTest: str
    :return: bool
    """
    digitCheck = re.compile(r"^.*?\d.*?")
    upperCaseCheck = re.compile(r"^.*?[A-Z].*?")
    lowerCaseCheck = re.compile(r"^.*?[a-z].*?")
    if len(stringToTest) < 8:
        return False
    if not digitCheck.search(stringToTest):
        return False
    if not upperCaseCheck.search(stringToTest):
        return False
    if not lowerCaseCheck.search(stringToTest):
        return False

    return True


def main():
    password = "Apples12"
    print(passwordStrengthDetector(password))

if __name__ == '__main__':
    main()