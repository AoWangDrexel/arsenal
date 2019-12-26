import numpy as np
from math import ceil
from random import randint
from cryptsenal import detect_english as de


"""The Columnar Transposition Cipher Module.

The Columnar Transposition Cipher implementation includes encryption and 
decryption methods.
"""


def order(word):
    """Returns the order the letter of the words alphabetically.
    
    Example
    =======
    >>> from cryptsenal.transposition import *
    >>> order("ZEBRAS")
    [5, 2, 1, 3, 0, 4]

    Args:
        word (str): A key.
        
    Returns:
        list: The sorting order.
    """
    letter_count, order_list = {}, []
    word_list = "".join(sorted([letter for letter in word]))
    for letter in word:
        if letter in letter_count.keys():
            letter_count[letter]+=1
        else:
            letter_count[letter] = word_list.find(letter)
        order_list.append(letter_count[letter])
    return order_list


def encrypt(plain_text, key):
    """Encrypts the plain text.
    
    Example
    =======
    >>> from crypsenal.transposition import *
    >>> encrypt("WE ARE DISCOVERED. FLEE AT ONCE.", "ZEBRAS")
    RCDENF IRL PEDEFT.ASEEOHEO. CRW V AE
    
    Args:
        plain_text (str): A plain text.
        key (str): A key string.
    
    Returns:
        str: A cipher text.
    """
    cipher_text, col = "", len(key)
    row = ceil(len(plain_text)/col)
    ordering = order(key)
    arr = np.full((row, col), " ")
    while col*row > len(plain_text):
        plain_text += chr(65+randint(0,25))
    for r in range(row):
        for c in range(col):
            arr[r,c] = plain_text[r*col+c]
    for c in range(col):
        for r in range(row):
            pos = ordering.index(c)
            cipher_text += arr[r, pos]
    return cipher_text


def decrypt(cipher_text, key):
    """Decrypts the cipher text.
    
    Example
    =======
    >>> from crypsenal.transposition import *
    >>> decrypt("RCDENF IRL PEDEFT.ASEEOHEO. CRW V AE", "ZEBRAS")
    WE ARE DISCOVERED. FLEE AT ONCE.PHFR
    
    Args:
        cipher_text (str): A cipher text.
        key (str): A key string.
        
    Returns:
        str: A plain text.
    """
    plain_text, col = "", len(key)
    row = ceil(len(cipher_text)/col)
    ordering = order(key)
    arr = np.full((row, col), " ")
    for c in range(col):
        for r in range(row):
            pos = ordering.index(c)
            arr[r, pos] = cipher_text[c*col+r]
    for i in range(row):
        for j in range(col):
            plain_text += arr[i,j]
    return plain_text