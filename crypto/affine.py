import cryptsenal.detect_english as de


"""The Affine Cipher Module.

The Affine Cipher Implementation has encrypytion and decryption methods,
along with a brute force module.
"""


def gcd(a, b):
    """Returns the greatest common divisor.
    
    Example
    =======
    >>> from cryptsenal.affine import *
    >>> gcd(15, 6)
    3
    
    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of the two numbers.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def mod_inverse(a, b):
    """Returns the modular inverse using Euclid's extended algorithm.
    
    Example
    =======
    >>> from cryptsenal.affine import *
    >>> mod_inverse(5, 26)
    21
    
    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The modular inverse.

    Note
    ====
    Pseudocode can be found here: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    t, newt, r, newr = 0, 1, b, a
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1:
        return "{} is not invertible".format(a)
    if t < 0:
        t += b
    return t


def encrypt(plain_text, key_a, key_b):
    """Encrypts the plain text.

    Example
    =======
    >>> from cryptsenal.affine import *
    >>> encrypt("How are you today? Will you be my friend?", 5, 18)
    Bky szm iko jkhsi? Ygvv iko xm ai rzgmfh?
    
    Args:
        plain_text (str): A plain text.
        key_a (int): A slope key.
        key_b (int): An intercept key.

    Returns:
        str: A cipher text. 
    """
    cipher_text = ""
    for symbol in plain_text:
        if symbol.isalpha():
            cipher_text += (
                chr(((((ord(symbol) - 65) * key_a) + key_b) % 26) + 65)
                if symbol.isupper()
                else chr(
                    ((((ord(symbol.upper()) - 65) * key_a) + key_b) % 26) + 65
                ).lower()
            )
        else:
            cipher_text += symbol
    return cipher_text


def decrypt(cipher_text, key_a, key_b):
    """Decrypts the cipher text.
    
    Example
    =======
    >>> from cryptsenal.affine import *
    >>> decrypt("Bky szm iko jkhsi? Ygvv iko xm ai rzgmfh?", 5, 18)
    How are you today? Will you be my friend?
    
    Args:
        cipher_text (str): A cipher text.
        key_a (int): A slope key
        key_b (int): An intercept key.

    Returns:
        str: A plain text.
    """
    plain_text = ""
    for symbol in cipher_text:
        if symbol.isalpha():
            plain_text += (
                chr((ord(symbol) - 65 - key_b) * mod_inverse(key_a, 26) % 26 + 65)
                if symbol.isupper()
                else chr(
                    (ord(symbol.upper()) - 65 - key_b) * mod_inverse(key_a, 26) % 26
                    + 65
                ).lower()
            )
        else:
            plain_text += symbol
    return plain_text


def brute_force(cipher_text):
    """The function returns the decrypted cipher text by testing all the possibilties for the two keys.
    
    Example
    =======
    >>> from cryptsenal.affine import *
    >>> brute_force("Bky szm iko jkhsi? Ygvv iko xm ai rzgmfh?")
    Key 1: 5
    Key 2: 18
    Percentage accuracy: 100.0
    How are you today? Will you be my friend?
    
    Args:
        cipher_text (str): the cipher text

    Returns:
        str: the decrypted cipher text
    """
    key1, percentages = 1, {}
    for key1 in range(26):
        if gcd(key1, 26) != 1:
            continue
        for key2 in range(26):
            if de.get_english_count(decrypt(cipher_text, key1, key2)) > 80:
                percentages[str(key1), str(key2)] = de.get_english_count(
                    decrypt(cipher_text, key1, key2)
                )
    key_list, val_list = list(percentages.keys()), list(percentages.values())
    key_break = key_list[val_list.index(max(percentages.values()))]
    print("Key 1: " + str(key_break[0]))
    print("Key 2: " + str(key_break[1]))
    print("Percentage accuracy: " + str(percentages[key_break]))
    return decrypt(cipher_text, int(key_break[0]), int(key_break[1]))