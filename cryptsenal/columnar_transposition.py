"""
description: columnar transposition cipher
author: ao wang
date: june 19, 2020
"""

from cryptsenal.cipher import Cipher
import numpy as np
import random
import math
import string


class ColumnarTransposition(Cipher):
    """The Columnar Transposition Cipher

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: str
    """

    def __init__(self, text, key):
        super().__init__(text, key)

    def __str__(self):
        return "Message: {}\nKey: {}".format(self.text, self.key)

    def completeTheSquare(self):
        arr = self.removePunctuation().upper()
        area = math.ceil(len(arr)/len(self.key)) * len(self.key)
        extra = area % len(arr)
        for i in range(extra):
            # random.choice(string.ascii_uppercase) or "X"
            arr += "X"
        return arr

    def encrypt(self):
        arr = self.completeTheSquare()
        ordering = np.array([self.charToInt(char)
                             for char in self.key]).argsort()
        col = len(self.key)
        row = len(arr)//col
        arr = np.array(list(arr)).reshape(row, col)[:, ordering]
        return "".join(list(arr.T.flatten()))

    def decrypt(self):
        arr = self.completeTheSquare()
        ordering = []
        sortedKey = sorted(self.key)

        for letter in self.key:
            idx = sortedKey.index(letter)
            ordering.append(idx)
            sortedKey[idx] = " "

        col = len(self.key)
        row = len(arr)//col
        arr = np.array(list(arr)).reshape(col, row).T
        arr = arr[:, ordering]
        return "".join(list(arr.flatten()))


if __name__ == "__main__":
    msg = "NALCIEHWTTDTTFSEELEEDSOAWFEAHL"
    key = "GERMAN"
    c = ColumnarTransposition(msg, key)
    print(c.decrypt())
