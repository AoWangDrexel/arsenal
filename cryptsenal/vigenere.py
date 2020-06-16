"""
description: vigenere cipher
author: ao wang
date: june 16, 2020
"""
from cipher import Cipher


class Vigenere(Cipher):
    def __init__(self, text, key):
        super().__init__(text)
        self.key = key

    def __str__(self):
        return "Text: {}, Key: {}".format(self.text, self.key)

    def encrypt(self):
        self.text = self.removePunctuation()
        self.text = [self.intToChar((self.charToInt(char) + self.charToInt(self.key[idx % len(self.key)])))
                     if char.isalpha() else char for (idx, char) in enumerate(self.text)]
        return "".join(self.text)

    def decrypt(self):
        self.text = self.removePunctuation()
        self.text = [self.intToChar((self.charToInt(char) - self.charToInt(self.key[idx % len(self.key)])))
                     if char.isalpha() else char for (idx, char) in enumerate(self.text)]
        return "".join(self.text)

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key


if __name__ == "__main__":
    v = Vigenere("DEFENDTHEEASTWALLOFTHECASTLE", "FORTIFICATION")
    print(v.encrypt())
