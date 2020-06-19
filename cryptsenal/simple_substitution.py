"""
description: simple substitution cipher
author: ao wang
date: june 18, 2020
"""

from cryptsenal.cipher import Cipher
import string


class SimpleSubstitution(Cipher):
    """The Simple Substitution class

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: str
    """

    def __init__(self, text, key):
        super().__init__(text, key.upper())

    def encrypt(self):
        arr = self.removePunctuation()
        arr = [self.key[self.charToInt(char)] for char in arr]
        return "".join(arr)

    def decrypt(self):
        arr = self.removePunctuation()
        arr = [string.ascii_uppercase[self.key.find(char)] for char in arr]
        return "".join(arr)


if __name__ == "__main__":
    plainText = "ATTACKONTHEDAYOFBLACKSON"
    print(SimpleSubstitution(plainText, "phqgiumeaylnofdxjkrcvstzwb").encrypt())
