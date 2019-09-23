"""
This module implements the International Morse Code on text

Example:
    $ python morse.py

    import morse
    print(morse.encode("Hello World"))
    > .... . .-.. .-.. --- | .-- --- .-. .-.. -..

Attributes:
    morse_dict: dict
        the dictionary version of the morseTable.txt

Methods:
    load_morse_table()
        Returns a dictionary of the Morse Code
    encode(plain_text)
        Returns the encoded text
    values_by_keys(value)
        Returns the key by getting the value of the dictionary
    decode(encoded_text)
        Returns the decoded Morse Code text
"""

morse_dict = {}


def load_morse_table():
    """The function retrieves the morse code from a text file and cleans it up so the letters
       can be stored in the keys and code into the values
    """
    codes = ""
    with open("morseTable.txt", "r") as code:
        codes = code.read()

    codes.split("\n")
    codes = codes.split()
    keys = []
    values = []

    for i in range(len(codes)):
        if(i % 2 == 0):
            keys.append(codes[i])
        else:
            values.append(codes[i])

    morse_dict = {}
    for i in range(len(keys)):
        morse_dict[keys[i]] = values[i]
    return morse_dict


morse_dict = load_morse_table()


def encode(plain_text):
    """
    The function encrypts the plaintext into ciphertext and returns the string.

    Args:
        plain_text (str): regular Latin alphabetic text

    Returns:
        str: The encoded plain_text

    Raises:
        AttributeError
            If plain_text is not a string type.
        TypeError
            If no plain_text is passed in as an argument.
    """
    word = ""
    plain_text = plain_text.upper()

    for letter in plain_text:
        if(letter in morse_dict):
            word += morse_dict.get(letter) + " "
        else:
            word += "| "
    return word


def values_by_keys(value):
    """The function returns the key by inputting a value of the key
       if values not in dictionary, return -1

       Args:
           value (str): The portion of the Morse code text

       Returns:
           str: The key of the dictionary identified by value

       Raises:
           TypeError
               If no value is passed in as an argument.
    """
    for keys, values in morse_dict.items():
        if(value == values):
            return keys
    return -1


def decode(encoded_text):
    """The function decodes the encoded message

    Args:
        encoded_text (str): The encoded Morse Code text

    Returns:
        str: The decoded Morse code text

    Raises:
        AttributeError
            If encoded_text is not a string type
        TypeError
            If no encoded_text is passed in as an argument.
    """
    decoded = ""
    encoded_text = encoded_text.split(" ")
    for code in encoded_text:
        if " " in code:
            decoded += " " + values_by_keys(code.strip())
        decoded += str(values_by_keys(code))

    decoded = decoded.replace("-1", " ")
    return decoded
