"""The Simple Substitution Module.

An implementation of the Simple Substition Cipher, including a key shuffler method, 
a key checker, decrypter, and encrypter.
"""


from random import shuffle


def load_alphabet():
    """Returns the capitalized alphabet.
    
    Example
    =======
    >>> from cryptsenal.simple_sub import *
    >>> get_alphabet()
    ['A', 'B', 'C', 'D', 'E'..., 'W', 'X', 'Y', 'Z']
    
    Args:
        None
    Returns:
        List (char): A list of the alphabet.
    """
    return "".join([chr(65 + i) for i in range(26)])


def key_shuffle():
    """Creates a random key from shuffling the alphabet.
    
    Example
    =======
    >>> from cryptsenal.simple_sub import *
    >>> key_shuffle()
    ZPYQAIGEHUSMRCFLWBOXJTNVDK
    
    Args:
        None.
    
    Returns:
        str: A randomized key.
    """
    alphabet = list(load_alphabet())
    shuffle(alphabet)
    return "".join(alphabet)


def key_check(key):
    """Checks the key if it is a usable key.
    
    Example
    =======
    >>> from cryptsenal.simple_sub import *
    >>> key_check("ZPYQAIGEHUSMRCFLWBOXJTNVDK")
    True
    
    Args:
        key (str): A key.
    
    Returns:
        bool: Returns True if key is usable, False otherwise.
    """
    return sorted(list(key.upper())) == list(load_alphabet())


def simple_sub(msg, key, mode="e"):
    """Encrypts and decrypts the text.
    
    Example
    =======
    >>> from cryptsenal.simple_sub import *
    >>> simple_sub("How are you today?", "ZPYQAIGEHUSMRCFLWBOXJTNVDK")
    Efn zba dfj xfqzd?
    
    >>> simple_sub("Efn zba dfj xfqzd?", "ZPYQAIGEHUSMRCFLWBOXJTNVDK", "d")
    How are you today?
    
    Args:
        plain_text (str): A message.
        key (str): A key.

    Returns:
        str: An encrypted or decrypted message.
    """
    converted_text = ""
    alphabet = load_alphabet()
    if key_check(key):
        if mode == "d":
            key, alphabet = alphabet, key
        for symbol in msg:
            if symbol.isalpha():
                converted_text += (
                    key[alphabet.find(symbol)]
                    if symbol.isupper()
                    else key[alphabet.lower().find(symbol)].lower()
                )
            else:
                converted_text += symbol
        return converted_text
    return "There was an error with the key. Please try again."