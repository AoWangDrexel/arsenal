"""The Vigenere Cipher Module.

A Vigenere Cipher Implementation that encrypts and decrypts messages.
"""


def encrypt(plain_text, key_word, mode="e"):
    """Encrypts the plain text.
    
    Example
    =======
    >>> from cryptsenal.vigenere import *
    >>> encrypt("The quick brown fox jumps over 13 lazy dogs.", "vigenere")
    Opk uhmto wzuaa jfb ecstf smim 13 tgdl hfkn.
    
    Args:
        plain_text (str): A plain text.
        key_word (str): A key.
        
    Returns:
        str: A cipher text.    
    """
    cipher_text, key_idx, key_word = "", 0, key_word.upper()
    for symbol in plain_text:
        if symbol.isalpha():
            cipher_text += (
                chr(
                    (
                        ord(symbol)
                        + (
                            ord(key_word[key_idx])
                            if mode == "e"
                            else -ord(key_word[key_idx])
                        )
                    )
                    % 26
                    + 65
                )
                if symbol.isupper()
                else chr(
                    (
                        ord(symbol.upper())
                        + (
                            ord(key_word[key_idx])
                            if mode == "e"
                            else -ord(key_word[key_idx])
                        )
                    )
                    % 26
                    + 65
                ).lower()
            )
            key_idx += 1
            key_idx %= len(key_word)
        else:
            cipher_text += symbol
    return cipher_text


def decrypt(cipher_text, key_word):
    """Decrypts the cipher text.
    
    Example
    =======
    >>> from cryptsenal.vigenere import *
    >>> decrypt("Opk uhmto wzuaa jfb ecstf smim 13 tgdl hfkn.", "vigenere")
    The quick brown fox jumps over 13 lazy dogs.
    
    Args:
        cipher_text (str): A cipher text.
        key_word (str): A key.
        
    Returns:
        str: A plain text.
    """
    return encrypt(cipher_text, key_word, "d")