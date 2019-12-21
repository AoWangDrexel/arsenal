import secrets

"""The One-Time Pad Cipher Implementation.

The module includes a key creation method in case the user does not want to make one. 
The encryption and decryption methods are one in the same. Overall, the One-Time Pad Cipher
is known as the perfect cipher, therefore there was not a breaker method. 
"""


def create_key(length):
    """Creates a random key the length of the message.
    
    Example
    =======
    >>> from cryptsenal.one_time_pad import * 
    >>> create_key(10)
    VIQDUHKNZX
    
    Args:
        length (int): The length of the message.
    
    Returns:
        str: The key length-sized of the message.
    """
    return "".join([chr(secrets.randbelow(26) + 65) for i in range(length)])


def count_letters(msg):
    """Counts the number of letters in the message.
    
    Example
    =======
    >>> from cryptsenal.one_time_pad import *
    >>> count_letters("The answers to the test are under the desk.")
    34
    
    Args:
        msg (str): The message text.
        
    Returns:
        str: The message text without any characters besides the letters.
    """
    count = 0
    for symbol in msg:
        if symbol.isalpha():
            count += 1
    return count


def one_time_pad(msg, key, mode="e"):
    """Decrypts or encrypts the text with the key.
    
    Example
    =======
    >>> from cryptsenal.one_time_pad import *
    >>> one_time_pad("The answers to the test are under the desk.", "ZEMBWOGOIXKEKFJNVMVFFWLRRTMFQEYLDK")
    Slq bjgcszp ds dmn gzeo fwa feuxd yxi bpvu.
    
    >>> one_time_pad("Slq bjgcszp ds dmn gzeo fwa feuxd yxi bpvu.", "ZEMBWOGOIXKEKFJNVMVFFWLRRTMFQEYLDK", "d")
    The answers to the test are under the desk.
    
    Args:
        msg (str): The message that the user wants to encrypt or decrypt.
        key (str): The key.
        mode="e" (chr): The mode whether to encrypt or decrypt.
        
    Returns:
        str: The decrypted or encrypted message.
    """
    converted_text = ""
    key_index = 0
    if len(key) != count_letters(msg):
        print("The key is not the same length as the text.")
    else:
        for symbol in msg:
            if symbol.isalpha():
                changed_text = chr(
                    (
                        (
                            ord(symbol.upper())
                            + (
                                ord(key[key_index])
                                if mode == "e"
                                else -ord(key[key_index])
                            )
                        )
                        % 26
                    )
                    + ord("A")
                )
                converted_text += (
                    changed_text if symbol.isupper() else changed_text.lower()
                )
                key_index += 1

            else:
                converted_text += symbol
    return converted_text