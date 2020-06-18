"""
description: caesar cipher
author: ao wang
date: june 16, 2020
"""
from cryptsenal.cipher import Cipher


class Caesar(Cipher):
    """The Caesar Cipher class

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: int
    """

    def __init__(self, text, key):
        super().__init__(text, key)

    def __str__(self):
        return "Text: {}, Key: {}".format(self.text, self.key)

    def encrypt(self):
        """Encrypts the plain text into cipher text

        :returns: the encrypted plain text
        :rtype: str
        """
        arr = self.removePunctuation()
        arr = [self.intToChar(self.charToInt(char) + self.key) for char in arr]
        return "".join(arr)

    def decrypt(self):
        """Decrypts the cipher text into plain text

        :returns: the decrypted cipher text
        :rtype: str
        """
        self.setKey(26-self.key)
        return self.encrypt()

    def getKey(self):
        return key

    def setKey(self, key):
        self.key = key


if __name__ == "__main__":
    caesar = Caesar("OCZLPDXFWMJRIAJSEPHKNJQZMOCZGVUTYJB", -5)
    print(caesar.decrypt())