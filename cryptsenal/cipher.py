"""
description: abstract base class to extend to all other cipher classes
author: ao wang
date: june 16, 2020
"""


import abc
import re
import string


class Cipher(metaclass=abc.ABCMeta):
    """An abstract base cipher class 

    :param text: plain/cipher text
    :type text: str
    """

    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key

    @abc.abstractmethod
    def encrypt(self):
        """Encrypts the plain text into cipher text"""
        pass

    @abc.abstractmethod
    def decrypt(self):
        """Decrypts the cipher text into plain text"""
        pass

    def removePunctuation(self):
        """Removes punctuation from the plain text

        :returns: the plain text with only alphanumeric characters
        :rtype: str
        """
        return re.sub("[^A-Z]", "", repr(self.text))

    def intToChar(self, num):
        """Converts integers into characters in the alphabet

        :param num: the number you're trying to convert
        :type num: int
        :returns: the letter at the number
        :rtype: str
        """
        return string.ascii_uppercase[num % 26]

    def charToInt(self, char):
        """Converts the character to an integer according to a dictionary

        :param char: the character you're trying to convert
        :type char: str
        :returns: the value at the character
        :rtype: int
        """
        char = char.upper()
        arr = {chr(ord('A')+i): i for i in range(26)}
        return arr[char]

    def getText(self):
        return self.text

    def setText(self, text):
        self.text = text

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key
