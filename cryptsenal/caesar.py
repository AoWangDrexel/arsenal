"""
description: caesar cipher
author: ao wang
date: june 16, 2020
"""


from cryptsenal.cipher import Cipher
import time


class Caesar(Cipher):
    """The Caesar Cipher class

    :param text: the plain/cipher text
    :type text: str
    :param key: the cipher key
    :type key: int
    """

    def __init__(self, text, key):
        super().__init__(text)
        self.key = key

    def __str__(self):
        return "Text: {}, Key: {}".format(self.text, self.key)

    def encrypt(self):
        self.text = self.removePunctuation()
        self.text = [self.intToChar((self.charToInt(char) + self.key))
                     if char.isalpha() else char for char in self.text]
        return "".join(self.text)

    def decrypt(self):
        self.text = self.removePunctuation()
        self.text = [self.intToChar((self.charToInt(char) - self.key))
                     if char.isalpha() else char for char in self.text]
        return "".join(self.text)

    def getKey(self):
        return key

    def setKey(self, key):
        self.key = key


if __name__ == "__main__":
    caesar = Caesar("defend the east wall of the castle", 12)
    print(caesar.encrypt())
    s = """Friends, Romans, countrymen, lend me your ears;
I come to bury Caesar, not to praise him.
The evil that men do lives after them;
The good is oft interred with their bones;
So let it be with Caesar. The noble Brutus
Hath told you Caesar was ambitious:
If it were so, it was a grievous fault,
And grievously hath Caesar answer’d it."""
    print(Caesar(s, 3).removePunctuation())