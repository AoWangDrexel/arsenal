from cryptsenal.cipher import Cipher
import numpy as np
import time


class RailFence(Cipher):
    def __init__(self, text, key):
        if key >= len(text):
            raise Exception(
                "The key is either the same size or larger than the text")
        super().__init__(text, key)

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
        fence = np.full((numOfRow, numOfCol), -1)
        rails = list(range(numOfRow-1)) + list(range(numOfRow-1, 0, -1))
        for idx, char in enumerate(text):
            fence[rails[idx % len(rails)], idx] = char
        fence = fence.flatten()
        return list(fence[fence != -1])


if __name__ == "__main__":
    plainText = "BEWARETHEBLACKSHEEP"
    msg = "breceeaehbakhewtlsp".upper()
    print(RailFence(msg, 3).decrypt())
