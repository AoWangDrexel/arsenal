"""
This module implements the Affine Cipher.

Example:
    $ python affine.py

    import affine
    print(affine.encrypt("Hello World", 5, 8))
    > Rclla Oaplx

Attributes:
    ALPHABET (str): the Latin alphabet

Methods:
    load_alphabet()
        Returns Latin alphabet
    gcd(num1, num2)
        Returns the greatest common divisor
    mod_inverse(num1, num2)
        Returns the modular inverse
    equation(num, slope, intercept)
        Returns integer after being multiplied by slope and added by intercept
    encrypt(plain_text, key_a, key_b)
        Returns encrypted plain text
    decrypt(cipher_text, key_a, key_b)
        Returns decrypted cipher text
    brute_force(cipher_text)
        Returns decrypted cipher text by testing all possibilites
"""


from crypto import detect_english as de

ALPHABET = ""


def load_alphabet():
    """The function loads the English alphabet
    """
    alphabet = ""
    for i in range(26):
        alphabet += chr(ord("a") + i)
    return alphabet


ALPHABET = load_alphabet()


def gcd(num1, num2):
    """The function returns the greatest common divisor using Euclid's algorithm.

        Args:
            num1 (int): the first number
            num2 (int): the second number

        Returns:
            int: the greatest common divisor of the two numbers

        Raises:
            TypeError
                If neither arguments are passed or neither arguments are integers.
    """
    while num1 != 0:
        num1, num2 = num2 % num1, num1
    return num2


def mod_inverse(num1, num2):
    """The function returns the modular inverse using Euclid's extended algorithm.

       Args:
           num1 (int): the first number
           num2 (int): the second number

       Returns:
           int: the modular inverse of the two numbers

       Raises:
           TypeError
               If neither arguments are passed or neither arguments are integers.
    """
    if gcd(num1, num2) != 1:
        return -1

    u1, u2, u3 = 1, 0, num1
    v1, v2, v3 = 0, 1, num2

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % num2


def equation(num, slope, intercept):
    """The function returns the integer used for the cipher using key1 and key2.

        Args:
            num (int): the number
            slope (int): the slope
            intercept (int): the intercept

        Returns:
            int: the result of the number multiplied by the slope and added by the intercept

        Raises:
            TypeError
                If all arguments are not passed or all arguments are not integers.
    """
    return slope * num + intercept


def encrypt(plain_text, key_a, key_b):
    """The function encrypts the plain text and returns the cipher text.

        Args:
            plain_text (str): the plain text
            key_a (int): the slope key
            key_b (int): the intercept key

        Returns:
            str: the encrypted plain text

        Raises:
            TypeError:
                If all arguments are not passed or plain_text is not a string type or key_a or key_b are neither int types.
    """
    cipher_text = ""
    for symbol in plain_text:
        if symbol.lower() in ALPHABET:
            idx = equation(
                ALPHABET.index(
                    symbol.lower()),
                key_a,
                key_b) % len(ALPHABET)
            if symbol.isupper():
                cipher_text += ALPHABET[idx].upper()
            else:
                cipher_text += ALPHABET[idx]
        else:
            cipher_text += symbol
    return cipher_text


def decrypt(cipher_text, key_a, key_b):
    """The function returns the decrypted cipher text.

        Args:
            cipher_text (str): the cipher text
            key_a (int): the slope key
            key_b (int): the intercept key

        Returns:
            str: the decrypted cipher text

        Raises:
            TypeError:
                If all arguments are not passed or cipher_text is not a string type or key_a or key_b are neither int types.
    """
    plain_text = ""
    for symbol in cipher_text:
        if symbol.lower() in ALPHABET:
            idx = abs(
                (ALPHABET.index(
                    symbol.lower()) -
                    key_b) *
                mod_inverse(
                    key_a,
                    len(ALPHABET)) %
                len(ALPHABET))
            if symbol.isupper():
                plain_text += ALPHABET[idx].upper()
            else:
                plain_text += ALPHABET[idx]
        else:
            plain_text += symbol
    return plain_text


def brute_force(cipher_text):
    """The function returns the decrypted cipher text by testing all the possibilties for the two keys.

       Args:
           cipher_text (str): the cipher text

       Returns:
           str: the decrypted cipher text

       Raises:
           TypeError
               If cipher_text is not passed in as an argument or cipher text is not a string type.
    """
    print("Hacking...")

    percentages = {}
    key1 = 1
    while key1 != 26:
        while gcd(key1, 26) != 1:
            key1 += 1

        for key2 in range(26):
            if de.get_english_count(decrypt(cipher_text, key1, key2)) > 80:
                percentages[str(key1) + " " + str(key2)
                            ] = de.get_english_count(decrypt(cipher_text, key1, key2))
        key1 += 1

    key_break = list(map(int, de.find_max_ind(percentages).split()))
    print("Key 1: " + str(key_break[0]))
    print("Key 2: " + str(key_break[1]))
    print("Percentage accuracy: " +
          str(percentages[de.find_max_ind(percentages)]))
    return decrypt(cipher_text, key_break[0], key_break[1])
