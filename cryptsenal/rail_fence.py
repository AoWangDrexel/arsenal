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
        numOfRow, numOfCol = self.key, len(self.text)
        fence = np.full((numOfRow, numOfCol), "")
        track, switchOrder = 0, True

        for idx, char in enumerate(arr):
            fence[track, idx] = char
            if track % (numOfRow - 1) == 0:
                switchOrder = not switchOrder

            if switchOrder:
                track -= 1
            else:
                track += 1

        fence = "".join(list(fence.flatten()))
        return fence

    def decrypt(self):
        arr = self.removePunctuation()
        numOfRow, numOfCol = self.key, len(self.text)
        fence = np.full((numOfRow, numOfCol), "")
        for idx, char in enumerate(arr):
            pass
        return super().decrypt()


if __name__ == "__main__":
    msg = "defend the east wall of the castle"
    key = 3
    t0 = time.time()
    print(RailFence(msg, key).encrypt())
    t1 = time.time()
    print(t1-t0)
