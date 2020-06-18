"""
description: affine cipher
author: ao wang
date: june 17, 2020
"""

from math import gcd
from sympy import mod_inverse
from cryptsenal.cipher import Cipher


class Affine(Cipher):
    """

    """

    def __init__(self, text, key):
        if gcd(key[0], 26) != 1:
            raise Exception(
                "a={} must be relatively prime to m=26".format(key[0]))
        super().__init__(text, key)

    def __str__(self):
        a, b = self.key
        return "text: {}, keys = [a: {}, b: {}]".format(self.text, a, b)

    def encrypt(self):
        a, b = self.key
        m = 26
        arr = self.removePunctuation()
        arr = [self.intToChar((a*self.charToInt(char)+b) % m) for char in arr]
        return "".join(arr)

    def decrypt(self):
        a, b = self.key
        m = 26
        arr = self.removePunctuation()
        arr = [self.intToChar(
            (mod_inverse(a, m)*(self.charToInt(char)-b)) % m) for char in arr]
        return "".join(arr)

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key


if __name__ == "__main__":
    a = Affine("ZRCKEWSGNPAOVHATBEQFUAJCPZRCLIDYXAM", (5, 8))
    print(a)
    print(a.decrypt())
