"""
This module implements the Caesar Cipher and multiple techniques to break the cipher, such as brute force with English detection and cryptanalysis.

Example:
    $ python caesar_cipher.py

    import caesar_cipher as cc
    print(cc.encrypt("Hello World", 2))
    > Jgnnq Yqtnf

Attributes:
    ALPHABET: str
        the lower and uppercase of the alphabet

Methods:
    load_alphabet()
        Returns a string of the lower and uppercase of the alphabet
    encrypt(plain_text, key)
        Returns the encrypted plain text
    symbol_count(text)
        Returns a dictionary of the symbol frequency
    decrypt(cipher_text, key)
        Returns the decrypted cipher text
    cryptanalysis(cipher_text)
        Returns the decrypted cipher text without the need of the key by finding the most
        frequent symbol
    brute_force(cipher_text)
        Returns the decrypted cipher text without the need of the key by testing keys: 0-25
"""
from crypto import detect_english as de

ALPHABET = ""


def load_alphabet():
    """The function loops through the ASCII code and returns a string of the
       lower and uppercase alphabet.
    """
    alphabet = ""
    for i in range(26):
        alphabet += chr(ord("A") + i)
        alphabet += chr(ord("a") + i)
    return alphabet


ALPHABET = load_alphabet()


def encrypt(plain_text, key):
    """The function encrypts the text with a certain key.

        Args:
            plain_text (str): The uncrypted message
            key (int): The integer shift of the alphabet

        Returns:
            str: The encrypted plain_text

        Raises:
            TypeError
                If plain_text or key is not passed through as an argument or
                if the plain_text is not a string type or key is not a integer type.

    """
    cipher_text = ""
    for letter in plain_text:
        if letter.isupper() and letter in ALPHABET:
            cipher_text += chr((ord(letter) + key - ord("A")) % 26 + ord("A"))
        elif letter.islower() and letter in ALPHABET:
            cipher_text += chr((ord(letter) + key - ord("a")) % 26 + ord("a"))
        else:
            cipher_text += letter
    return cipher_text


def symbol_count(text):
    """The function returns a dictionary that counts the frequency of the alphabet and symbols.

       Args:
           text (str): The string of text

       Returns:
           dict: The dictionary counting the frequency of the alphabet in the text

       Raises:
           AttributeError
               If text is not passed as a string type.
           TypeError
               If text is not passed as an argument.

    """
    letter_dict = {}
    text = text.upper()
    for letter in text:
        if letter in ALPHABET:
            if letter not in letter_dict.keys():
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict


def decrypt(cipher_text, key):
    """The function decrypts the cipher text given the key and returns the decrypted message.

       Args:
           cipher_text (str): The encrypted text
           key (int): The key used to shift the text

       Returns:
           str: The decrypted text

       Raises:
           TypeError
               If cipher_text or key is not passed through as an argument or
               if the cipher_text is not a string type or key is not a integer type.
    """

    while(key < 0):
        key += 26

    if key > 0:
        key = 26 - key

    return encrypt(cipher_text, key)


def cryptanalysis(cipher_text):
    """The function decrypts the cipher by finding the most frequent letter. However this
       method does not always work depending on the length of the cipher text. If the text is long
       there is a greater chance of decryption.

       Args:
           cipher_text (str): encrypted text

       Returns:
           str: decrypted text

       Raises:
           TypeError
               If cipher_text is not passed as an argument or not a string type.
    """
    alphabet = []
    high = 0
    high_key = ""

    for letter in range(26):
        alphabet.append(chr(ord("A") + letter))

    letter_dict = symbol_count(cipher_text)

    for keys in letter_dict.keys():
        if letter_dict.get(keys) > high:
            high = letter_dict.get(keys)
            high_key = keys

    break_key = alphabet.index(high_key) - alphabet.index("E")

    if break_key <= 0:
        break_key += 26
    return encrypt(cipher_text, 26 - break_key)


def brute_force(cipher_text):
    """The function prints out all the possibilities of the cipher by testing keys from 0-25.

       Args:
           cipher_text (str): Encrypted text

       Returns:
           str: Decrypted cipher message

       Raises:
           TypeError
               If cipher_text is not passed as an argument or cipher_text is not a string
    """
    print("Hacking...")

    percentages = {}
    for key in range(1, 26):
        decrypted_text = encrypt(cipher_text, key)

        threshold = 80
        if de.get_english_count(decrypted_text) > threshold:
            percentages[key] = de.get_english_count(decrypted_text)

    key_break = de.find_max_ind(percentages)

    if key_break != -1:
        print("Cipher hacked! :)\n")
        print("The key is: " + str(26 - key_break))
        print(
            "Decrypted text: " +
            encrypt(
                cipher_text,
                key_break) +
            "\n")
        print("Percentage of words in dictionary: " +
              str(percentages[key_break]))
    else:
        print("Failed to hack cipher :(")
