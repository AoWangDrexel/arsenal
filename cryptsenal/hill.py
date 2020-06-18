"""
description: abstract base class to extend to all other cipher classes
author: ao wang
date: june 18, 2020
"""

from cryptsenal.cipher import Cipher
from sympy import Matrix, mod_inverse
import string
import random
import timeit


class Hill(Cipher):
    def __init__(self, text, key):
        key = Matrix(key)
        row, column = key.shape
        if row != column:
            raise("Dimensions of the key are not a square matrix")
        super().__init__(text, key)

    def _matchDimension(self):
        arr = self.removePunctuation()
        evenDimensions = len(arr) % self.key.shape[0]
        if evenDimensions != 0:
            arr += "".join([random.choice(string.ascii_letters).upper()
                            for i in range(evenDimensions)])
        return arr

    def encrypt(self):
        cipherText = ""
        keyDim = self.key.shape[0]
        arr = [self.charToInt(char) for char in self._matchDimension()]
        for idx in range(0, len(arr), keyDim):
            cText = self.key * Matrix((arr[idx: idx+keyDim]))
            for i in list(cText):
                cipherText += self.intToChar(i % 26)
        return cipherText

    def decrypt(self):
        plainText = ""
        keyDim = self.key.shape[0]
        kInverse = self.key.adjugate() * mod_inverse(self.key.det(), 26)
        arr = [self.charToInt(char) for char in self._matchDimension()]
        for idx in range(0, len(arr), keyDim):
            cText = kInverse * Matrix(arr[idx: idx+keyDim])
            for i in list(cText):
                plainText += self.intToChar(i % 26)
        return plainText


if __name__ == "__main__":
    key = [[5, 17], [4, 15]]
    msg = "OGTVZKCWQF"
    h = Hill(msg, key)
    print(h.decrypt())
