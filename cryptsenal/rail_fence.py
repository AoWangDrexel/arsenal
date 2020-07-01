"""
description: railfence cipher
author: ao wang
date: june 23, 2020
"""

from cryptsenal.cipher import Cipher
import numpy as np
import time


class RailFence(Cipher):
    """The RailFence Cipher class

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: int
    """

    def __init__(self, text, key):
        if key >= len(text):
            raise Exception(
                "The key is either the same size or larger than the text")
        super().__init__(text, key)

    def __str__(self):
        return "Message: {}\nKey: {}".format(self.text, self.key)

    def encrypt(self):
        arr = self.removePunctuation()
        return "".join(self.createFence(arr))

    def decrypt(self):
        arr = self.removePunctuation()
        ind = list(range(len(arr)))
        pos = self.createFence(ind)
        return "".join([arr[pos.index(i)] for i in ind])

    def createFence(self, text):
        numOfRow, numOfCol = self.key, len(text)
        if type(text[0]) == int:
            fence = np.full((numOfRow, numOfCol), -1)
        else:
            fence = np.full((numOfRow, numOfCol), "")

        rails = list(range(numOfRow-1)) + list(range(numOfRow-1, 0, -1))

        for idx, char in enumerate(text):
            fence[rails[idx % len(rails)], idx] = char

        fence = fence.flatten()
        return list(fence[fence != -1]) if (type(text[0]) == int) else list(fence[fence != ""])


if __name__ == "__main__":
    plainText = "BEWARETHEBLACKSHEEP"
    msg = "breceeaehbakhewtlsp".upper()
    r = RailFence(msg, 3)
    print(r.decrypt())
