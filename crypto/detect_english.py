"""
This module implements English detection using two English dictionary text files.

Attributes:
    LETTERS_AND_SPACE: str
        makeup of the alphabet and any white space
    ENGLISH_WORDS: list
        collection of the English words from the two text files

Methods:
    load_alphabet()
        Returns a string of the lower and uppercase of the alphabet
    load_dictionary()
        Returns a list of English words
    remove_non_letters(msg)
        Returns message without any non-alphabetic symbols
    get_english_count(msg)
        Returns a percentage of the number of words in the English dictionary
        out of total number of words in the message
    find_max_ind(keys)
        Returns the index of the greatest percentage decrypted message from the list
"""

LETTERS_AND_SPACE = ""


def load_alphabet():
    """The function loops through the ASCII code and returns a string of the
       lower and uppercase alphabet.
    """
    alphabet = ""
    for i in range(26):
        alphabet += chr(ord("A") + i)
        alphabet += chr(ord("a") + i)
    return alphabet


def load_dictionary():
    """The function returns a list of words from two word text files.
    """
    with open("words.txt", "r") as f1, \
            open("morewords.txt", "r") as f2:
        file1 = f1.read().split("\n")
        file2 = f2.read().split("\n")

    for i in range(len(file2)):
        file2[i] = file2[i].lower()

    file2.extend(file1)
    return file2


LETTERS_AND_SPACE = load_alphabet() + " \t\n"
ENGLISH_WORDS = load_dictionary()


def remove_non_letters(msg):
    """The function removes non characters in the LETTERS_AND_SPACE variable.

    Args:
        msg (str): English text

    Returns:
        str: English text without any other non-alphabetic symbols

    Raises:
        TypeError
            If msg is not passed as an argument or msg is not a string type
    """
    lettersOnly = []
    for symbol in msg:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return "".join(lettersOnly)


def get_english_count(msg):
    """The function returns the percentage of words in the dictionary.

    Args:
        msg (str): English text

    Returns:
        double: Percentage of words in the English dictionary from total number of words in msg

    Raises:
        TypeError
            If msg is not passed as an argument or msg is not a string type
    """
    msg = msg.lower()
    msg = remove_non_letters(msg)
    possibleWords = msg.split()
    if possibleWords == []:
        return 0
    matches = 0

    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return 100 * float(matches) / len(possibleWords)


def find_max_ind(keys):
    """The function finds the highest percentage of words in the dictionary and returns the key

        Args:
            keys (list): list of percentages of the possibilities of English text

        Returns:
            int: the index of the highest percentage

        Raises:
            TypeError:
                If keys is not passed as an argument or keys is not a list
    """
    maximum = -1
    max_key = -1
    for key in keys:
        if keys[key] > maximum:
            maximum = keys[key]
            max_key = key
    return max_key
